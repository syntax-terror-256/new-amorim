from django.urls import path
from .views import *

app_name = "cardapio"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("detalhes/<str:type>/<int:pk>", DetailView.as_view(), name="details"),
]
