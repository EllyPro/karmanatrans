# Generated by Django 4.0.2 on 2022-02-20 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blok', '0007_alter_cars_driver_name_alter_drivers_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='litsence',
            name='comments',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментария'),
        ),
        migrations.AddField(
            model_name='putyovka',
            name='comments',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментария'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='state_number',
            field=models.CharField(max_length=8, unique=True, verbose_name='Hомер автомобиля'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='tex_passport_number',
            field=models.CharField(max_length=10, unique=True, verbose_name='Hомер техпаспорта'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='type_of_car',
            field=models.CharField(max_length=20, verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='litsence',
            name='car_state_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blok.cars', verbose_name='Hомер автомобиля'),
        ),
        migrations.AlterField(
            model_name='litsence',
            name='deadline_date',
            field=models.DateField(verbose_name='Cрок дата'),
        ),
        migrations.AlterField(
            model_name='litsence',
            name='given_date',
            field=models.DateField(verbose_name='Данная дата'),
        ),
        migrations.AlterField(
            model_name='putyovka',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='putyovka',
            name='money',
            field=models.IntegerField(verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='putyovka',
            name='state_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blok.cars', verbose_name='Hомер автомобиля'),
        ),
    ]
