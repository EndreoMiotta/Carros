# Generated by Django 4.2.1 on 2023-06-25 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='car',
            name='factory_year',
            field=models.IntegerField(verbose_name='Ano de Fabricação'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=200, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.IntegerField(verbose_name='Ano do Modelo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(upload_to='cars/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.FloatField(verbose_name='Valor'),
        ),
    ]
