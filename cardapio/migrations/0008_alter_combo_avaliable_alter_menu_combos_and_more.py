# Generated by Django 5.2.1 on 2025-06-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardapio", "0007_combo_maximum_optionals_quantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="combo",
            name="avaliable",
            field=models.BooleanField(default=True, verbose_name="disponível"),
        ),
        migrations.AlterField(
            model_name="menu",
            name="combos",
            field=models.ManyToManyField(
                default=None,
                related_name="menus",
                to="cardapio.combo",
                verbose_name="cardápio",
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="products",
            field=models.ManyToManyField(
                default=None,
                related_name="menus",
                to="cardapio.product",
                verbose_name="cardápio",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="avaliable",
            field=models.BooleanField(default=True, verbose_name="disponível"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.CharField(
                default="/static/cardapio/img/coming-soon-placeholder.png",
                verbose_name="url da imagem",
            ),
        ),
    ]
