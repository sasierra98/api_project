from django.db import models
from django.utils.translation import gettext_lazy as _

from product_api.models.category import Category


class Product(models.Model):
    """Model of Products"""

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )

    category = models.ForeignKey(
        to=Category,
        verbose_name=_('Category'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'
