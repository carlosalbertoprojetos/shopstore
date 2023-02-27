from django.db import models
from django.urls import reverse_lazy as _



class UnitMeasure(models.Model):
    name = models.CharField( max_length=50)
    abbreviation = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def unit_gau_edit(self):
        return _('product:unit_update', args=[self.pk])

    def unit_gau_delete(self):
        return _('product:unit_delete', args=[self.pk])


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def prodcat_gau_edit(self):
        return _('product:prodcat_update', args=[self.pk])

    def prodcat_gau_delete(self):
        return _('product:prodcat_delete', args=[self.pk])


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True)
    valueBuy = models.DecimalField(max_digits=9, decimal_places=2)
    valueSell = models.DecimalField(max_digits=9, decimal_places=2)
    details = models.CharField(max_length=255, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    available = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    createdin = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name

    def product_gau_detail(self):
        return _('product:product_details', args=[self.pk])

    def product_gau_edit(self):
        return _('product:product_update', args=[self.pk])

    def product_gau_delete(self):
        return _('product:product_delete', args=[self.pk])


    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.name,
            'estoque': self.stock,
        }
