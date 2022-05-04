from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class Suppliers(models.Model):
    company = models.CharField(
        verbose_name=_('Company'),
        max_length=255,
    )

    email = models.CharField(
        verbose_name=_('Email'),
        max_length=255,
        unique=True
    )

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=255,
        default='',
        blank=True
    )

    cellphone = models.CharField(
        verbose_name=_('Cellphone'),
        max_length=255,
        default='',
        blank=True
    )

    address = models.TextField(
        verbose_name=_('Address'),
        default='',
        blank=True
    )

    country = CountryField(
        verbose_name=_('Country'),
    )

    is_active = models.BooleanField(
        verbose_name=_("It's Active"),
        default=True
    )

    nit = models.CharField(
        verbose_name=_('Nit'),
        blank=True,
        default='',
        max_length=255
    )

    website = models.CharField(
        verbose_name=_('Website'),
        blank=True,
        default='',
        max_length=255
    )

    def __str__(self) -> str:
        return f'{self.pk} | {self.company}'



