from rest_framework import serializers
from .models import Categoria, Producto
from .validators import validar_nombre

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


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[validar_nombre])
    email = serializers.EmailField()
    message = serializers.CharField()