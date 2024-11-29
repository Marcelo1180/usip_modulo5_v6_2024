from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductoSerializer, ReporteProductoSerializer, ContactSerializer

from .forms import ProductoForm
from .models import Categoria, Producto
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsUserAlmacen
from .utils import permission_required
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello World")

def contact(request, name):
    return HttpResponse(f"Hello {name}")

def categorias(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    categorias = Categoria.objects.all()
    return render(request, "form_categorias.html", {
        "categorias": categorias
    })

def productoFormView(request):
    form = ProductoForm()
    producto = None
    id_producto = request.GET.get("id")

    if id_producto:
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductoForm(instance=producto)

    if request.method == "POST":
        if producto:
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)

    if form.is_valid():
        form.save()
    return render(request, "form_productos.html", {"form": form})


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def categoria_count(request):
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse({"cantidad": cantidad}, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)

@api_view(['GET'])
def producto_en_unidades(request):
    try:
        productos = Producto.objects.filter(unidades='u')
        return JsonResponse(ProductoSerializer(productos, many=True).data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)


@api_view(['GET'])
@permission_required(['inventario.reporte_cantidad'])
def reporte_producto(request):
    try:
        productos = Producto.objects.filter(unidades='u')
        logger.info(f"Productos encontrados: {productos.count()}")
        return JsonResponse(ReporteProductoSerializer({"cantidad": productos.count(), "productos": productos}).data, safe=False, status=200)
    except Exception as e:
        logger.error(f"Error en reporte_producto: {e}")
        return JsonResponse({"error": str(e)}, safe=False, status=500)


@api_view(['POST'])
@permission_classes([IsUserAlmacen])
def enviar_mensaje(request):
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({"mensaje": "Mensaje enviado correctamente"}, status=200)
    else:
        return JsonResponse({"mensaje": cs.errors}, status=200)