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
    minimum = models.FloatField(default=1, verbose_name="quantidade mínima")
    avaliable = models.BooleanField(default=True, verbose_name="disponível")

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
    avaliable = models.BooleanField(default=True, verbose_name="disponível")
    minimum_optionals_quantity = models.IntegerField(
        verbose_name="quantidade mínima de opcionais", default=1
    )
    maximum_optionals_quantity = models.IntegerField(
        verbose_name="quantidade máxima de opcionais", default=255
    )

    included_products = models.ManyToManyField(
        Product,
        through="ComboProduct",
        through_fields=("combo", "included_product"),
        blank=True,
        symmetrical=False,
        verbose_name="Produtos Inclusos",
    )

    included_combos = models.ManyToManyField(
        "self",
        through="ComboCombo",
        through_fields=("combo", "included_combo"),
        blank=True,
        symmetrical=False,
        verbose_name="Combos Inclusos",
    )

    class Meta:
        verbose_name = "Combo"

    def __str__(self):
        return self.name


class ComboProduct(models.Model):
    combo = models.ForeignKey(
        Combo, on_delete=models.CASCADE, related_name="included_combo"
    )
    included_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="produto incluso"
    )

    optional = models.BooleanField(default=False, verbose_name="opcional")


class ComboCombo(models.Model):
    combo = models.ForeignKey(
        Combo, on_delete=models.CASCADE, related_name="included_product"
    )
    included_combo = models.ForeignKey(
        Combo, on_delete=models.CASCADE, verbose_name="combo incluso"
    )

    optional = models.BooleanField(default=False, verbose_name="opcional")


# model que representa um cardápio, usado para categorizar produtos
# somente produtos pertencentes a um cardápio são exibidos na página do cardápio, isso vale para produtos e combos
# produtos e cardápios possuem uma relação M2M
# combos e cardápios possuem uma relação M2M
class Menu(models.Model):
    name = models.CharField(verbose_name="nome")
    products = models.ManyToManyField(
        Product, default=None, related_name="menus", verbose_name="cardápio"
    )
    combos = models.ManyToManyField(
        Combo, default=None, related_name="menus", verbose_name="cardápio"
    )

    class Meta:
        verbose_name = "Cardápio"

    def __str__(self):
        return self.name
