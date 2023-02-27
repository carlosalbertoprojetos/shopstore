from django.db import models
from django.urls.base import reverse_lazy as _

from order.models import Order



class Bank(models.Model):
    name = models.CharField( max_length=50)
    number = models.CharField(max_length=10)
    agency = models.CharField(max_length=8)
    details = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    createdin = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
        ordering = ['-createdin']

    def __str__(self):
        return self.name

    def bank_gau_detail(self):
        return _('financial:bank_details', args=[self.pk])

    def bank_gau_edit(self):
        return _('financial:bank_update', args=[self.pk])

    def bank_gau_delete(self):
        return _('financial:bank_delete', args=[self.pk])


class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='banks')
    name = models.CharField( max_length=50)
    description = models.CharField(max_length=100, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0) 
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    createdin = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['-createdin']

    def __str__(self):
        return self.name

    def account_gau_detail(self):
        return _('financial:account_details', args=[self.pk])

    def account_gau_edit(self):
        return _('financial:account_update', args=[self.pk])

    def account_gau_delete(self):
        return _('financial:account_delete', args=[self.pk])


class DestinationCategory(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=255, null=True, blank=True)

    def destcat_gau_edit(self):
        return _('financial:destcat_update', args=[self.pk])

    def destcat_gau_delete(self):
        return _('financial:destcat_delete', args=[self.pk])

class Destination(models.Model):
    name = models.CharField( max_length=50)
    category = models.ForeignKey(DestinationCategory, on_delete=models.CASCADE)
    details = models.CharField(max_length=255, null=True, blank=True)

    def dest_gau_edit(self):
        return _('financial:destination_update', args=[self.pk])

    def dest_gau_delete(self):
        return _('financial:destination_delete', args=[self.pk])

class Release(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    date = models.DateField()
    description = models.CharField(max_length=100, blank=True)
    valueorder = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    installments = models.CharField(max_length=2, blank=True)
    totalorder = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    details = models.CharField(max_length=255, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    createdin = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    def release_gau_edit(self):
        return _('financial:release_update', args=[self.pk])

    def release_gau_delete(self):
        return _('financial:release_delete', args=[self.pk])

    class Meta:
        ordering = ['-createdin']


class FormPayment(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Form Payment'
        verbose_name_plural = 'Forms Payments'

    def __str__(self):
        return self.name

    def formpayment_gau_edit(self):
        return _('financial:Payment_update', args=[self.pk])

    def formpayment_gau_delete(self):
        return _('financial:payment_delete', args=[self.pk])


class Payment(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='release')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account')
    date = models.DateField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    details = models.CharField(max_length=255, null=True, blank=True)
    formpayment = models.ForeignKey(FormPayment, on_delete=models.CASCADE, max_length=255)
    updated = models.DateTimeField(auto_now=True)
    createdin = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-createdin']

    def __str__(self):
        return self.name

    def payment_gau_detail(self):
        return _('financial:payment_details', args=[self.pk])

    def payment_gau_edit(self):
        return _('financial:Payment_update', args=[self.pk])

    def payment_gau_delete(self):
        return _('financial:payment_delete', args=[self.pk])