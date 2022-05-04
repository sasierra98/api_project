from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        """Create new user"""

        if not email:
            raise ValueError(_('Email is necessary'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create superuser"""

        user = self.create_user(email=self.normalize_email(email), name=name, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Model of Users"""

    email = models.CharField(
        verbose_name=_('Email'),
        max_length=255,
        unique=True
    )

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        default=''
    )

    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=255,
    )

    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=255,
    )

    identification = models.IntegerField(
        verbose_name=_('Identification'),
        blank=True,
        null=True,
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

    country = models.ForeignKey(
        to='cities_light.Country',
        verbose_name=_('Country'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    state = models.ForeignKey(
        to='cities_light.Region',
        verbose_name=_('State'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    city = models.ForeignKey(
        to='cities_light.City',
        verbose_name=_('City'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    genre = models.TextField(
        verbose_name=_('Genre'),
        default='',
        blank=True
    )

    is_active = models.BooleanField(
        verbose_name=_("It's Active"),
        default=True
    )

    is_staff = models.BooleanField(
        verbose_name=_("It's Staff"),
        default=False
    )

    is_customer = models.BooleanField(
        verbose_name=_("It's a customer"),
        default=False
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name

    def __str__(self):
        # return f'{self.first_name} {self.last_name} | {self.identification}'
        return f'{self.name} | {self.identification}'
