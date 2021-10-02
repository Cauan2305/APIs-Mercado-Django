from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ProdutosSerializer
from .models import Produto
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import  Response

# class ProdutoViewsets(viewsets.ModelViewSet):
#     serializer_class=ProdutosSerializer
#     queryset=Produto.objects.all()
    
    # def get_queryset(self):
    #     queryset=Produto.objects.all()
    #     username=self.request.query_params.get('nome')
    #     if username is not None:
    #         queryset=queryset.filter(purchaser__username=username)
    #     return queryset

# class ProdutoViewsets(ListAPIView):
#     serializer_class=ProdutosSerializer
#     queryset=Produto.objects.all()
#     filter_backends=(SearchFilter,OrderingFilter)
#     search_fields = ('nome','categoria')


# class ProdutoViewsets(generics.ListCreateAPIView):
    
#         serializer_class=ProdutosSerializer
#         queryset=Produto.objects.all()
#         filter_backends=(SearchFilter,OrderingFilter)
#         search_fields = ('nome','categoria')


# class ProdutosViewsets(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class=ProdutosSerializer
#     queryset=Produto.objects.all()
        


class ProdutoViewsets(viewsets.ModelViewSet):
        
        permission_classes=(IsAuthenticated,)
        serializer_class=ProdutosSerializer
        queryset=Produto.objects.all()

class index(APIView)    :
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Produto.objects.all()
        return Response({'produto': queryset})


