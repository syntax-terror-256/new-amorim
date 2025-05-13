from django.views import View
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Product, Menu


class IndexView(View):
    def get(self, request: HttpRequest):
        menus = Menu.objects.all()
        context = {
            "menus": menus,
        }
        return render(request, "cardapio/index.html", context)
