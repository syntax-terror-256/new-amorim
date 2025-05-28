from enum import Enum

from django.db import models


# model que representa um produto, seja ele encomendável ou parte de um conjunto
class Product(models.Model):
    class ProductChoices(models.IntegerChoices):
        unidade = 0, "unidade"
        cento = 1, "cento"
        kg = 2, "kg"

    name = models.CharField(verbose_name="nome")
    image = models.CharField(
        verbose_name="url da imagem",
        default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png",
    )
    details = models.CharField(verbose_name="detalhes")
    price = models.FloatField(verbose_name="preço")
    unit_type = models.IntegerField(
        verbose_name="tipo de unidade",
        choices=ProductChoices,
        default=ProductChoices.unidade,
    )
    minimum = models.FloatField(verbose_name="quantidade mínima", default=1)
    avaliable = models.BooleanField(verbose_name="disponível")

    class Meta:
        verbose_name = "Produto"

    def __str__(self):
        return self.name


# model que representa um combo, podendo ser qualquer combinação de produtos e/ou outros combos
class Combo(models.Model):
    name = models.CharField(verbose_name="nome")
    image = models.CharField(
        verbose_name="url da imagem",
        default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png",
    )
    details = models.CharField(verbose_name="detalhes")
    price = models.FloatField(verbose_name="preço")
    avaliable = models.BooleanField(verbose_name="disponível")

    class Meta:
        verbose_name = "Combo"

    def __str__(self):
        return self.name


# model que representa um cardápio, usado para categorizar produtos
# somente produtos pertencentes a um cardápio são exibidos na página do cardápio, isso vale para produtos e combos
# produtos e cardápios possuem uma relação M2M
# combos e cardápios possuem uma relação M2M
class Menu(models.Model):
    name = models.CharField(verbose_name="nome")
    products = models.ManyToManyField(Product, default=None, related_name="menus")
    combos = models.ManyToManyField(Combo, default=None, related_name="menus")

    class Meta:
        verbose_name = "Cardápio"

    def __str__(self):
        return self.name
