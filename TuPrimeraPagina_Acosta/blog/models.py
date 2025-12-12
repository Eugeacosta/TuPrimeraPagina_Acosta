from django.db import models

# Modelo 1: Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo 2: Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre

# Modelo 3: Post
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    
    def __str__(self):
        return f"{self.titulo} ({self.fecha_publicacion})"
