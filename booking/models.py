from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Booking(models.Model):

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

    date_until = models.DateTimeField(
        verbose_name=_('Booking date'),
        blank=True, null=True,
    )

    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True,
    )

    booking_id = models.CharField(
        max_length=100,
        verbose_name=_('Booking ID'),
        blank=True,
    )

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return '#{} ({})'.format(self.booking_id or self.pk,
                                 self.creation_date)
