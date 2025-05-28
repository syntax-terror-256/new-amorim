from django.contrib import admin

from .models import Product, Combo, Menu


# usado para exibir os cardápios associados a um produto no painel do produto
class MenuProductModelInline(admin.TabularInline):
    verbose_name = "Cardápios Associados"
    verbose_name_plural = verbose_name
    model = Product.menus.through
    extra = 1


# usado para exibir os cardápios associados a um combo no painel do combo
class MenuComboModelInline(admin.TabularInline):
    verbose_name = "Cardápios Associados"
    verbose_name_plural = verbose_name
    model = Combo.menus.through
    extra = 1


# usado para exibir os produtos associados a um cardápio no painel do cardápio
# substitui o fórmulário padrão por um mais funcional e intuitivo
class ProductModelInline(admin.TabularInline):
    verbose_name = "Produtos Associados"
    verbose_name_plural = verbose_name
    model = Menu.products.through
    extra = 1


# usado para exibir os combos associados a um cardápio no painel do cardápio
# substitui o fórmulário padrão por um mais funcional e intuitivo
class ComboModelInline(admin.TabularInline):
    verbose_name = "Combos Associados"
    verbose_name_plural = verbose_name
    model = Menu.combos.through
    extra = 1


# registra models no painel de admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MenuProductModelInline]


@admin.register(Combo)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MenuComboModelInline]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [ProductModelInline, ComboModelInline]
    exclude = ["products", "combos"]
