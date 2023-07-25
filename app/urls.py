from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import login_view, logout_view, register_view
from cars.views import (CarDeleteView, CarDetailView, CarsListView,
                        CarUpdateView, NewCarCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarsListView.as_view(), name='cars_list'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('register/', register_view, name='register'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('login/', login_view, name='login'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('logout/', logout_view, name='logout'),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
