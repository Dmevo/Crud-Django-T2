from django.db import models

# Create your models here.

class Produto(models.Model):

    nome = models.CharField(max_length=45)
    quant_estoque = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.TextField()
    ativo = models.BooleanField()

class PedidoItem(models.Model):

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=6, decimal_places=2)
    desconto = models.DecimalField(max_digits=3, decimal_places=2)

class Pedido(models.Model):

    pedido_item = models.ForeignKey(PedidoItem, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    ativo = models.BooleanField()
