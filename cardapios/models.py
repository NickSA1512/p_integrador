from django.db import models


class Cardapio(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.nome

class Segmento(models.Model):
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Item(models.Model):
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    info = models.CharField(max_length=2000, blank=True, null=True, verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name= "Preço")
    imagem = models.ImageField(upload_to="", blank=True, null=True)
    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    info = models.CharField(max_length=2000, blank=True, null=True, verbose_name="Descrição")
    UF =  models.CharField(max_length=2)
    cidade = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    rua = models.CharField(max_length=300)
    numero = models.IntegerField(verbose_name="Número")
    def __str__(self):
        return self.nome

class CardapioLink(models.Model):
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    def __str__(self):
        return self.cardapio