# Generated by Django 4.0.5 on 2022-06-03 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('quant_estoque', models.IntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=6)),
                ('imagem', models.TextField()),
                ('ativo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=3)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ativo', models.BooleanField()),
                ('pedido_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.pedidoitem')),
            ],
        ),
    ]
