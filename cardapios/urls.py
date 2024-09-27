from django.urls import path
from . import views

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("restaurantes/", views.index, name="index"),
    path("cardapios/<str:nome>/", views.cardapio, name="cardapio"),
    path("media/<str:imagem>/",views.media, name="media")
]