from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)



urlpatterns = [
    path('contact/<str:name>', views.contact),
    # path('categorias/', views.categorias, name="categoria"),
    # path('productos/', views.productoFormView, name="producto"),
    # path('', views.index),
    #path('', include(router.urls)),
    path('categoria/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('categoria/count/', views.categoria_count, name='categoria-count'),
    path('producto/filtrar/unidades/', views.producto_en_unidades, name='producto-unidades'),
    path('producto/reporte/', views.reporte_producto, name='producto-reporte'),
    path('contact/', views.enviar_mensaje, name='contact'),
]
