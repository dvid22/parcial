from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import (
    AutorSerializer, EditorialSerializer, LibroSerializer,
    MiembroSerializer, PrestamoSerializer
)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['autor', 'editorial']   # 👈 filtrar por FK
    search_fields = ['titulo', 'isbn']          # 👈 búsqueda por texto


class MiembroViewSet(viewsets.ModelViewSet):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fecha_prestamo', 'miembro']   # 👈 filtrar préstamos
