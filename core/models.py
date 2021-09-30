from django.db import models

Categoria_choices=(
    ('H','Hortifruti'),
    ('C','Carnes',),
    ('F','Frios'),
    ('U','Utensilos'),


)

# class Categoria(models.Model):
#     nome=models.CharField(choices=Categoria_choices,max_length=10)


class Produto (models.Model):
    nome=models.CharField(max_length=100)
    preco=models.FloatField()
    categoria=models.CharField(choices=Categoria_choices,max_length=10)




    class Meta :
        verbose_name='Produto'
        verbose_name_plural='Produtos'



    def __str__(self):
        return self.nome