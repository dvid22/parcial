from rest_framework import serializers
from .models import Autor, Editorial, Libro, Miembro, Prestamo


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    # Mostrar datos del autor y editorial en la respuesta
    autor = AutorSerializer(read_only=True)
    editorial = EditorialSerializer(read_only=True)

    # Permitir crear libros indicando solo los IDs de autor y editorial
    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(), source='autor', write_only=True
    )
    editorial_id = serializers.PrimaryKeyRelatedField(
        queryset=Editorial.objects.all(), source='editorial', write_only=True
    )

    class Meta:
        model = Libro
        fields = [
            'id_libro',  # 👈 usa el nombre real de la PK en tu modelo
            'titulo', 
            'resumen', 
            'isbn', 
            'anio_publicacion',
            'autor', 
            'editorial', 
            'autor_id', 
            'editorial_id'
        ]


class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class PrestamoSerializer(serializers.ModelSerializer):
    # Mostrar información del libro y del miembro
    libro = LibroSerializer(read_only=True)
    miembro = MiembroSerializer(read_only=True)

    # Para crear un préstamo solo pedimos los IDs
    libro_id = serializers.PrimaryKeyRelatedField(
        queryset=Libro.objects.all(), source='libro', write_only=True
    )
    miembro_id = serializers.PrimaryKeyRelatedField(
        queryset=Miembro.objects.all(), source='miembro', write_only=True
    )

    class Meta:
        model = Prestamo
        fields = [
            'id_prestamo',   # 👈 igual aquí: usa el nombre de la PK en tu modelo
            'fecha_prestamo', 
            'fecha_devolucion',
            'libro', 
            'miembro', 
            'libro_id', 
            'miembro_id'
        ]
