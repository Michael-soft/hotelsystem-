# Generated by Django 4.0.5 on 2022-06-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_app', '0002_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]
