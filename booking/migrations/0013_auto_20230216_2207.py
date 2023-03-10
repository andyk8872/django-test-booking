# Generated by Django 3.2.17 on 2023-02-16 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20230216_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='creation_date',
            field=models.DateField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='timeslot',
            field=models.IntegerField(choices=[(1, '18:00'), (2, '18:30'), (3, '19:00'), (4, '19:30'), (5, '20:00'), (6, '20:30'), (7, '21:00'), (8, '21:30'), (8, '22:00')], default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_guests',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='No. Of Guests(Max = 12)'),
        ),
    ]
