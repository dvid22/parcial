# 📚 API Biblioteca - Documentación

Esta API permite gestionar autores, libros, personas, tareas y préstamos de una biblioteca.  
Todos los servicios responden en formato *JSON*.

---

## 🔑 Endpoints

### 1. Autores
- *Listar autores*
  - GET http://127.0.0.1:8000/api/autores/
- *Crear autor*
  - POST http://127.0.0.1:8000/api/autores/
  - Body:
    json
    {
      "nombre": "Gabriel García Márquez"
    }
    
- *Detalle de un autor*
  - GET http://127.0.0.1:8000/api/autores/{id}/
- *Actualizar autor*
  - PUT http://127.0.0.1:8000/api/autores/{id}/
  - Body:
    json
    {
      "nombre": "Isabel Allende"
    }
    
- *Eliminar autor*
  - DELETE http://127.0.0.1:8000/api/autores/{id}/

---

### 2. Libros
- *Listar libros*
  - GET http://127.0.0.1:8000/api/libros/
- *Crear libro*
  - POST http://127.0.0.1:8000/api/libros/
  - Body:
    json
    {
      "titulo": "Cien Años de Soledad",
      "autor": 1,
      "anio_publicacion": 1967,
      "genero": "Novela"
    }
    
- *Detalle de un libro*
  - GET http://127.0.0.1:8000/api/libros/{id}/
- *Actualizar libro*
  - PUT http://127.0.0.1:8000/api/libros/{id}/
- *Eliminar libro*
  - DELETE http://127.0.0.1:8000/api/libros/{id}/

---

### 3. Personas
- *Listar personas*
  - GET http://127.0.0.1:8000/api/personas/
- *Crear persona*
  - POST http://127.0.0.1:8000/api/personas/
  - Body:
    json
    {
      "nombre": "Sergio Nieto",
      "correo": "sergio@example.com"
    }
    
- *Detalle de persona*
  - GET http://127.0.0.1:8000/api/personas/{id}/
- *Actualizar persona*
  - PUT http://127.0.0.1:8000/api/personas/{id}/
- *Eliminar persona*
  - DELETE http://127.0.0.1:8000/api/personas/{id}/
- *Filtrar persona por nombre*
  - GET http://127.0.0.1:8000/api/personas?nombre=sergio

---

### 4. Tareas
- *Listar tareas*
  - GET http://127.0.0.1:8000/api/tareas/
- *Crear tarea*
  - POST http://127.0.0.1:8000/api/tareas/
  - Body:
    json
    {
      "titulo": "Revisar inventario",
      "descripcion": "Verificar stock de libros",
      "fecha": "2025-09-04"
    }
    
- *Detalle de tarea*
  - GET http://127.0.0.1:8000/api/tareas/{id}/
- *Actualizar tarea*
  - PUT http://127.0.0.1:8000/api/tareas/{id}/
- *Eliminar tarea*
  - DELETE http://127.0.0.1:8000/api/tareas/{id}/
- *Filtrar tareas por fecha*
  - GET http://127.0.0.1:8000/api/tareas?fecha=2025-09-04

---

### 5. Préstamos
- *Listar préstamos*
  - GET http://127.0.0.1:8000/api/prestamos/
- *Crear préstamo*
  - POST http://127.0.0.1:8000/api/prestamos/
  - Body:
    json
    {
      "libro": 1,
      "persona": 2,
      "fecha_prestamo": "2025-09-04",
      "fecha_devolucion": "2025-09-18",
      "estado": "activo"
    }
    
- *Detalle de préstamo*
  - GET http://127.0.0.1:8000/api/prestamos/{id}/
- *Actualizar préstamo*
  - PUT http://127.0.0.1:8000/api/prestamos/{id}/
- *Eliminar préstamo*
  - DELETE http://127.0.0.1:8000/api/prestamos/{id}/

---

## ⚙ Respuestas comunes

- *200 OK* → Petición exitosa  
- *201 Created* → Registro creado correctamente  
- *400 Bad Request* → Error en los datos enviados  
- *404 Not Found* → Recurso no encontrado  
- *500 Internal Server Error* → Error interno del servidor  

---

## 🛠 Recomendaciones
- Usar Postman o cURL para probar los endpoints.  
- Siempre enviar datos en formato application/json.  
- Validar que libro y persona existan antes de crear un préstamo.

Para saber mas información en postman ingresa al siguiente link:https://serniet22-6135841.postman.co/workspace/0dc71281-47ce-40c6-8b57-47159d18c6d9/collection/48003272-64b403e7-d3f6-4971-af11-384ab65b9ba4?action=share&source=copy-link&creator=48003272 