from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Model of Categories"""

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )

    def __str__(self):
        return f'{self.pk} | {self.name}'
