from django.contrib import admin

from .models import Product, Menu


# usado para exibir os cardápios associados a um produto no painel do produto
class MenuModelInline(admin.TabularInline):
    verbose_name = "Cardápios Associados"
    verbose_name_plural = verbose_name
    model = Product.menus.through
    extra = 1


# usado para exibir os produtos associados a um cardápio no painel do cardápio
# substitui o fórmulário padrão por um mais funcional e intuitivo
class ProductModelInline(admin.TabularInline):
    verbose_name = "Produtos Associados"
    verbose_name_plural = verbose_name
    model = Menu.products.through
    extra = 1


# registra models no painel de admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MenuModelInline]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [ProductModelInline]
    exclude = ["products"]
