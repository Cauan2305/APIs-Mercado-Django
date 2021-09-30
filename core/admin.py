from django.contrib import admin
from .models import *



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('nome','preco','categoria')