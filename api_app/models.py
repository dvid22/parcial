from django.db import models


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, db_column="T001IdAutor")
    nombre = models.CharField(max_length=100, db_column="T001Nombre")
    apellido = models.CharField(max_length=100, db_column="T001Apellido")
    biografia = models.TextField(null=True, blank=True, db_column="T001Biografia")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = "T001Autor"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, db_column="T002IdEditorial")
    nombre = models.CharField(max_length=150, db_column="T002Nombre")
    direccion = models.CharField(max_length=255, db_column="T002Direccion")
    telefono = models.CharField(max_length=20, null=True, blank=True, db_column="T002Telefono")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "T002Editorial"
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, db_column="T003IdLibro")
    titulo = models.CharField(max_length=200, db_column="T003Titulo")
    resumen = models.TextField(null=True, blank=True, db_column="T003Resumen")
    isbn = models.CharField(max_length=20, unique=True, db_column="T003ISBN")
    anio_publicacion = models.PositiveIntegerField(db_column="T003AnioPublicacion")

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="libros",
        db_column="T003IdAutor"
    )
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        related_name="libros",
        db_column="T003IdEditorial"
    )

    def __str__(self):
        return f"{self.titulo} ({self.anio_publicacion})"

    class Meta:
        db_table = "T003Libro"
        verbose_name = "Libro"
        verbose_name_plural = "Libros"


class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True, db_column="T004IdMiembro")
    nombre = models.CharField(max_length=100, db_column="T004Nombre")
    apellido = models.CharField(max_length=100, db_column="T004Apellido")
    email = models.EmailField(unique=True, db_column="T004Email")
    fecha_membresia = models.DateField(db_column="T004FechaMembresia")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = "T004Miembro"
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True, db_column="T005IdPrestamo")
    fecha_prestamo = models.DateField(db_column="T005FechaPrestamo")
    fecha_devolucion = models.DateField(null=True, blank=True, db_column="T005FechaDevolucion")

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="prestamos",
        db_column="T005IdLibro"
    )
    miembro = models.ForeignKey(
        Miembro,
        on_delete=models.CASCADE,
        related_name="prestamos",
        db_column="T005IdMiembro"
    )

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} a {self.miembro.nombre} el {self.fecha_prestamo}"

    class Meta:
        db_table = "T005Prestamo"
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"

