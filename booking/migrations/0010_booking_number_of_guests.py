# Generated by Django 3.2.17 on 2023-02-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_remove_booking_number_of_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number_of_guests',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='No. Of Guests(Max = 12)'),
        ),
    ]