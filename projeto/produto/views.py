from django.shortcuts import render, redirect
from produto.forms import ProdutoForm
from produto.models import Produto

def index(request):
    return render(request, "index.html")

def ver_produtos(request):
    produto_list = Produto.objects.all()

    return render(request, "produtos.html", {"produto_list":produto_list})


def ver_formulario(request):
    produto_form = ProdutoForm()
    
    return render(request, "adicionar.html", {"produto_form":produto_form})


def adicionar_produto(request):
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            estoque = form.cleaned_data['quant_estoque']
            preco = form.cleaned_data['preco_unitario']
            img = form.cleaned_data['imagem']
            ativo = form.cleaned_data['ativo']
            
            produto = Produto(None, nome, estoque, preco, img, ativo)
            produto.save()

    return render(request, "index.html")


def procurar_produto(request):
    if request.method == 'POST':
        pesquisa = request.POST.get['pesquisa']
        produto_list = Produto.objects.filter(nome=pesquisa)

    return render(request, "index.html", {"produto_list":produto_list})
 

# Create your views here.
