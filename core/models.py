# core/models.py
from django.db import models

class Produto(models.Model):
    """
    Entidade representativa do catálogo corporativo da JWC Tecnologia.
    Mapeada diretamente para a tabela core_produto no banco relacional.
    """
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da Solução"
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço Unitário (R$)"
    )
    descricao = models.TextField(
        verbose_name="Descrição Detalhada do Serviço"
    )
    disponivel = models.BooleanField(
        default=True,
        verbose_name="Disponível para Venda"
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos e Soluções"
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"