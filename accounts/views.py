from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token

from .forms import CustomAuthenticationForm


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = authenticate(request,
                                username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password1'])
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                messages.success(request,
                                 f"Registro bem-sucedido! Seu token é: {token.key}")
            return redirect('cars_list')
    else:
        user_form = UserCreationForm()

    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        login_form = CustomAuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user = authenticate(request,
                                username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            token = login_form.cleaned_data['token']

            if user is not None and Token.objects.filter(key=token,
                                                         user=user).exists():
                login(request, user)
                return redirect('cars_list')

    else:
        login_form = CustomAuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('cars_list')
