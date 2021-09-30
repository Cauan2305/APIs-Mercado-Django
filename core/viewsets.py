from rest_framework import viewsets
from .serializers import ProdutosSerializer
from .models import Produto
class ProdutoViewsets(viewsets.ModelViewSet):
    serializer_class=ProdutosSerializer
    queryset=Produto.objects.all()