from django.db import models
from django.utils.translation import gettext_lazy as _

from product_api.models.category import Category
from user_api.models import Suppliers


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

    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        default=''
    )

    image = models.ImageField(
        blank=True,
        null=True
    )

    unit_price = models.FloatField(
        verbose_name=_('Unitary Price'),
        default=0.0
    )

    sell_price = models.FloatField(
        verbose_name=_('Sell Price'),
        default=0.0
    )

    quantity = models.IntegerField(
        verbose_name=_('Quantity'),
        default=0
    )

    supplier = models.ForeignKey(
        to=Suppliers,
        verbose_name=_('Supplier'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    in_stock = models.BooleanField(
        verbose_name='In stock',
        default=False
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()

        if self.quantity != 0:
            self.in_stock = True
        else:
            self.in_stock = False

    def __str__(self):
        return f'{self.name}'
