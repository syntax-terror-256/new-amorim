import typing

from django.views import View
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict

from .models import Product, Combo, Menu


class IndexView(View):
    def get(self, request: HttpRequest):
        menus = Menu.objects.all()
        context = {
            "menus": menus,
        }
        return render(request, "cardapio/index.html", context)


class DetailView(View):
    def get(
        self,
        request: HttpRequest,
        type: typing.Literal["combo", "produto"],
        pk: int,
    ):
        match type:
            case "combo":
                obj = get_object_or_404(Combo, pk=pk)

                menus = Menu.objects.all()
                context = {
                    "type": "combo",
                    "instance": obj,
                }
                return render(request, "cardapio/details.html", context=context)

            case "produto":
                obj = get_object_or_404(Product, pk=pk)

                menus = Menu.objects.all()
                context = {
                    "type": "product",
                    "instance": obj,
                }
                return render(request, "cardapio/details.html", context=context)

            case _:
                return HttpResponseBadRequest(f"'{type}' is not a valid product type")
