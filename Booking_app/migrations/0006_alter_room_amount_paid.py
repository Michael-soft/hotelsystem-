# Generated by Django 4.0.5 on 2022-06-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_app', '0005_room_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='amount_paid',
            field=models.IntegerField(),
        ),
    ]