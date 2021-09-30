from rest_framework import serializers
from .models import Produto,Categoria_choices
from rest_framework.renderers import JSONRenderer

class ProdutosSerializer(serializers.ModelSerializer):
    # nome=serializers.CharField(max_length=100)
    # preco=serializers.FloatField()
    # categoria=serializers.CharField(choices=Categoria_choices,max_length=10)

    class Meta:
        model=Produto
        fields='__all__'
        

# serializer=ProdutosSerializer(Produto)
# serializer.data

# json=JSONRenderer().render(serializer.data)
