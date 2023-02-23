from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy as _


from register.models import Register
from product.models import Product
from .managers import EstoqueEntradaManager, EstoqueSaidaManager

from store.constant import MOVIMENT_CHOICES, OPERATION_TYPE


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class Order(models.Model):
    date = models.DateField()
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
    operation = models.CharField(max_length=100, choices=OPERATION_TYPE)
    details = models.CharField(max_length=255, null=True, blank=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    updated = models.DateTimeField(auto_now=True)
    createdin = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-date']

    def __str__(self):
        return str(self.register)

    def order_gau_detail(self):
        return _('order:order_details', args=[self.pk])

    def order_gau_edit(self):
        return _('order:order_update', args=[self.pk])

    def order_gau_delete(self):
        return _('order:order_delete', args=[self.pk])


# Create your models here.
class ProductOrder(models.Model):


    pass


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENT_CHOICES, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} --- {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '---'


class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'


class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque saída'
        verbose_name_plural = 'estoque saída'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)


class ProtocoloEntrega(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estoque_atualizado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    # def get_absolute_url(self):
    #     return reverse_lazy('estoque:protocolo_de_entrega_detail', kwargs={'pk': self.pk})