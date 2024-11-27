from django.test import TestCase
from .models import Categoria
from django.core.exceptions import ValidationError


class TestCategoria(TestCase):
    # fixtures = ["dump_inventario.json"]

    # def setUp(self):
    #     self.categoria = Categoria.objects.create(nombre="Golosinas")

    def test_grabacion(self):
        categoria = Categoria(nombre="Bebidas")
        categoria.save()
        self.assertEqual(Categoria.objects.count(), 1)

    def test_validacion_categoria(self):
        with self.assertRaises(ValidationError) as qv:
            q = Categoria.objects.create(nombre="No permitido")
            q.full_clean()
        
        mensaje = dict(qv.exception)
        self.assertEqual(mensaje["nombre"][0], "No es una opcion permitida")
