from django.db import models
from django.urls import reverse
from django.urls.base import reverse_lazy as _


class Bank(models.Model):
    name = models.CharField( max_length=50)
    number = models.CharField(max_length=10)
    agency = models.CharField(max_length=8)
    detail = models.CharField(max_length=255, null=True, blank=True)
    createdin = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def bank_gau_detail(self):
        return reverse('financial:bank_details', args=[self.pk])

    def bank_gau_edit(self):
        return reverse('financial:bank_update', args=[self.pk])

    def bank_gau_delete(self):
        return reverse('financial:bank_delete', args=[self.pk])

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
        ordering = ['-createdin']


class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='banks')
    name = models.CharField( max_length=50)
    description = models.CharField(max_length=100, blank=True)
    detail = models.CharField(max_length=255, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0) 
    active = models.BooleanField(default=True)
    createdin = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.bank,'-',self.name

    def account_gau_detail(self):
        return reverse('financial:account_details', args=[self.pk])

    def account_gau_edit(self):
        return reverse('financial:account_update', args=[self.pk])

    def account_gau_delete(self):
        return reverse('financial:account_delete', args=[self.pk])

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['-createdin']


class Release(models.Model):

    TIPO_CHOICE = [
        ('credit','Credit'),
        ('debit','Debit'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accounts')
    date = models.DateField()
    release = models.CharField(max_length=20, choices=TIPO_CHOICE)
    description = models.CharField(max_length=100, blank=True)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    detail = models.CharField(max_length=255, null=True, blank=True)
    share = models.BooleanField(default=False, blank=True)    
    createdin = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.release) or str(self.description)

    def get_absolute_url(self):
        return _('financial:lancamento_detalhes', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-createdin']

    def save(self, *args, **kwargs):
        if self.release == 'debit':
            self.value = (self.value * -1)
        elif self.release == 'credit' and self.value < 0:
            self.value = (self.value * +1)
        
        self.account.balance += self.value
        self.account.save()
        return super(Release, self).save(*args, **kwargs)


class ExpenseCategory(models.Model):
    name = models.CharField( max_length=50)
    detail = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Expense category'
        verbose_name_plural = 'Category expenses'
        ordering = ['name']


class Expense(models.Model):
    name = models.CharField( max_length=50)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering = ['name']