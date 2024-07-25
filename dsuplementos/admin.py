from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'marca', 'descricao', 'preco', 'imagem']
    search_fields = ['produto', 'marca', 'descricao', 'preco', 'imagem']