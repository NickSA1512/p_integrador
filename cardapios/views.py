from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, FileResponse
from mysite.settings import MEDIA_ROOT
from .models import Cardapio, Segmento, Item, Restaurante, CardapioLink
from django.views import generic
import os


def frontpage(request):
    return render(request, "cardapios/frontpage.html")


def index(request):
    cardapio = Cardapio.objects.all()
    restaurante = Restaurante.objects.all()
    link = CardapioLink.objects.all()
    UFget = Restaurante.objects.values_list("UF", flat=True)
    context = {
        "cardapio":cardapio,
        "restaurante":restaurante,
        "link":link,
        "UFget":UFget,
    }
    return render(request, "cardapios/index.html", context)


def cardapio(request, nome):
    cardapio = get_object_or_404(Cardapio, nome=nome)
    segmento = Segmento.objects.all()
    item = Item.objects.all()
    context = {
        "cardapio":cardapio,
        "segmento":segmento,
        "item":item,
    }
    return render(request, "cardapios/cardapio.html", context)


def media(request, imagem):
    return FileResponse(open(os.path.join(MEDIA_ROOT, imagem), 'rb'))

