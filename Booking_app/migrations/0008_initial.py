# Generated by Django 4.0.5 on 2022-06-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Booking_app', '0007_delete_contact_delete_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('occupant_name', models.CharField(help_text='your name,surname first', max_length=100)),
                ('occupant_email', models.EmailField(max_length=254)),
                ('occupant_occupation', models.CharField(max_length=100)),
                ('number_of_night', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]
