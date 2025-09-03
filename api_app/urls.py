from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, EditorialViewSet, LibroViewSet, MiembroViewSet, PrestamoViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'editoriales', EditorialViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'miembros', MiembroViewSet)
router.register(r'prestamos', PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
