from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .viewsets import ProdutoViewsets,index

router=SimpleRouter()
router.register('produto',ProdutoViewsets)


urlpatterns = [
    path('index',index.as_view()),
    # path('produto/<int:pk>/',ProdutosViewsets.as_view(),name='produtos'),
]