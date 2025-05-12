from enum import Enum

from django.db import models


# model que representa um produto, seja ele encomendável ou parte de um conjunto
class Product(models.Model):
    class ProductChoices(models.IntegerChoices):
        unidade = 0, "unidade"
        cento = 1, "cento"
        kg = 2, "kg"

    name = models.CharField(verbose_name="nome")
    price = models.FloatField(verbose_name="preço")
    unit_type = models.IntegerField(
        verbose_name="tipo de unidade",
        choices=ProductChoices,
        default=ProductChoices.unidade,
    )
    minimum = models.FloatField(verbose_name="quantidade mínima", default=0)
    avaliable = models.BooleanField(verbose_name="disponibilidade")

    class Meta:
        verbose_name = "Produto"

    def __str__(self):
        return self.name


# model que representa um cardápio, usado para categorizar produtos
# produtos e cardápios possuem uma relação M2M
class Menu(models.Model):
    name = models.CharField(verbose_name="nome")
    products = models.ManyToManyField(Product, default=None, related_name="menus")

    class Meta:
        verbose_name = "Cardápio"

    def __str__(self):
        return self.name
