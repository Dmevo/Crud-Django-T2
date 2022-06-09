from socket import fromshare
from django import forms
from produto.models import Produto, PedidoItem, Pedido

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        
        fields = [
            'nome',
            'quant_estoque',
            'preco_unitario',
            'imagem',
            'ativo',
        ]

class PedidoItemForm(forms.ModelForm):

    class Meta:

        fields = [
            'produto',
            'quantidade',
            'desconto',
        ]

class PedidoForm(forms.ModelForm):

    class Meta:

        fields = [
            'pedido_item',
            'data_criacao',
            'valor_total',
            'ativo',
        ]