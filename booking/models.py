from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Booking(models.Model):

    TIMESLOT_LIST = (
        (1, '18:00'),
        (2, '18:30'),
        (3, '19:00'),
        (4, '19:30'),
        (5, '20:00'),
        (6, '20:30'),
        (7, '21:00'),
        (8, '21:30'),
        (8, '22:00'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User name'),
        related_name='bookings',
        blank=True, null=True,
    )

    forename = models.CharField(
        verbose_name=_('First name'),
        max_length=20,
        blank=True,
    )

    surname = models.CharField(
        verbose_name=_('Last name'),
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
    )

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=256,
        blank=True,
    )

    date_until = models.DateField(
        verbose_name=_('Booking date'),
        blank=True, null=True,
    )

    timeslot = models.IntegerField(
        verbose_name=_('Booking time'),
        default=0,
        choices=TIMESLOT_LIST)

    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True,
    )  

    total_guests = models.IntegerField(
        verbose_name=('No. Of Guests(Max = 12)'),
        default=1,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ],
        blank=True, null=True,
    )     

    class Meta:
        ordering = ['-creation_date']

    # def __str__(self):
    #     return '#{} ({})'.format(self.user or self.pk,
    #                              self.creation_date)

    def __str__(self):
        return (str(self.user))
