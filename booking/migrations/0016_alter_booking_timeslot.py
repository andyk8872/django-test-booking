# Generated by Django 3.2.17 on 2023-02-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20230216_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timeslot',
            field=models.IntegerField(choices=[(1, '18:00'), (2, '18:30'), (3, '19:00'), (4, '19:30'), (5, '20:00'), (6, '20:30'), (7, '21:00'), (8, '21:30'), (8, '22:00')], default=0, verbose_name='Booking time'),
        ),
    ]
