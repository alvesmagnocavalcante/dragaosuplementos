from django.db import models


class Produto(models.Model):
    produto = models.CharField(max_length=255, verbose_name='Produto')
    marca = models.CharField(max_length=255, verbose_name='marca')
    descricao = models.TextField(max_length=1000, verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    imagem = models.ImageField(upload_to='imagens/', default=None)
    
    def __str__(self):
        return self.produto