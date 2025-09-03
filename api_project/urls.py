from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return HttpResponse("""
        <h1>Bienvenido a la API de Biblioteca 📚</h1>
        <p>Usa los siguientes enlaces para acceder a los endpoints:</p>
        <ul>
            <li><a href="/api/autores/">Autores</a></li>
            <li><a href="/api/editoriales/">Editoriales</a></li>
            <li><a href="/api/libros/">Libros</a></li>
            <li><a href="/api/miembros/">Miembros</a></li>
            <li><a href="/api/prestamos/">Préstamos</a></li>
        </ul>
        <p>También puedes entrar al <a href="/admin/">Panel de Administración</a></p>
    """)

urlpatterns = [
    path('', home),  # Página de inicio
    path('admin/', admin.site.urls),
    path('api/', include('api_app.urls')),
]
