from django.db import models
from django.templatetags.static import static


# model que representa um produto, seja ele encomendável ou parte de um conjunto
class Product(models.Model):
    class ProductChoices(models.IntegerChoices):
        unidade = 0, "unidade"
        cento = 1, "cento"
        kg = 2, "kg"

    name = models.CharField(verbose_name="nome")
    image = models.CharField(
        verbose_name="url da imagem",
        default=static("cardapio/img/coming-soon-placeholder.png"),
    )
    details = models.CharField(verbose_name="detalhes")
    description = models.TextField(verbose_name="descrição")
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


# model que representa um combo composto por:
# - imagem, nome, descrição, preço e disponibilidade
# - produtos inclusos e suas quantidades exatas
# - outros combos inclusos e suas quantidades exatas
# - produtos que podem ser personalizados (ex: cauda de chocolate ou morango)
# - itens opcionais (ex: incluir sachês de ketchup)
class Combo(models.Model):
    name = models.CharField(verbose_name="nome")
    image = models.CharField(
        verbose_name="url da imagem",
        default=static("cardapio/img/coming-soon-placeholder.png"),
    )
    details = models.CharField(verbose_name="detalhes")
    price = models.FloatField(verbose_name="preço")
    avaliable = models.BooleanField(default=True, verbose_name="disponível")

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

    included_choices = models.ManyToManyField(
        "ComboChoices", verbose_name="Campos Personalizáveis"
    )
    # TODO: Optionals

    class Meta:
        verbose_name = "Combo"

    def __str__(self):
        return self.name


# model que representa produtos de quantidade fixa inclusos no combo
class ComboProduct(models.Model):
    combo = models.ForeignKey(
        Combo, on_delete=models.CASCADE, related_name="included_product"
    )
    included_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="produto incluso"
    )
    quantity = models.IntegerField(verbose_name="quantidade", default=0)


# model que representa combos de quantidade fixa inclusos no combo
class ComboCombo(models.Model):
    combo = models.ForeignKey(
        Combo, on_delete=models.CASCADE, related_name="included_combo"
    )
    included_combo = models.ForeignKey(
        Combo, on_delete=models.CASCADE, verbose_name="combo incluso"
    )
    quantity = models.IntegerField(verbose_name="quantidade", default=0)


class ComboChoices(models.Model):
    title = models.CharField(verbose_name="título")
    description = models.TextField(verbose_name="descrição")
    minimun_choices = models.IntegerField(
        verbose_name="quantidade mínima de escolhas", default=0
    )
    maximun_choices = models.IntegerField(
        verbose_name="quantidade máxima de escolhas", default=255
    )
    included_products = models.ManyToManyField(
        Product,
        through="ComboChoicesProduct",
        through_fields=("combo_choice", "included_product"),
        blank=True,
        symmetrical=False,
        verbose_name="Produtos Inclusos",
    )

    class Meta:
        verbose_name = "Campo Personalizável de Combo"

    def __str__(self):
        return self.title


class ComboChoicesProduct(models.Model):
    combo_choice = models.ForeignKey(
        ComboChoices, on_delete=models.CASCADE, related_name="included_product"
    )
    included_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="produto incluso"
    )
    selected = models.BooleanField(verbose_name="selecionado")


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
