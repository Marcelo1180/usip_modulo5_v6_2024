from rest_framework import serializers
from .models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ReporteProductoSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    productos = ProductoSerializer(many=True)