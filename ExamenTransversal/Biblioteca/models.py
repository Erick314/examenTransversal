from django.db import models

class NavItem (models.Model):
    idNavItem = models.AutoField(db_column="id_nav_item", primary_key=True)
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=150)

class Libro (models.Model):
    idLibro = models.AutoField(db_column="id_libro", primary_key=True)
    titulo = models.CharField(max_length=100)
    anioPublicacion = models.CharField(max_length=4)
    descripcion = models.TextField()

class Autor (models.Model):
    idAutor = models.AutoField(db_column="id_autor", primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

class Categoria (models.Model):
    idCategoria = models.AutoField(db_column="id_categoria", primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()