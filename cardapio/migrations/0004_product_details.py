# Generated by Django 5.2 on 2025-05-13 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardapio", "0003_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="details",
            field=models.CharField(
                default="Descrição genérica para testes.", verbose_name="detalhes"
            ),
            preserve_default=False,
        ),
    ]
