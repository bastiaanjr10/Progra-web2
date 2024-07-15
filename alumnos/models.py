from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

##Test usuarios

class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(
        primary_key=True, db_column='idTipo', verbose_name='ID_tipo_Usuario')
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoUsuario)



class Usuario(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    appPaterno = models.CharField(max_length=30, blank=False, null=False)
    appMaterno = models.CharField(max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    tipoUsuario = models.ForeignKey(
        'tipoUsuario', on_delete=models.CASCADE, db_column='idTipo')
    correo = models.EmailField(
        unique=True, blank=False, null=False, max_length=100)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.appPaterno)+" "+str(self.appMaterno)
    

#Models producto inventario
    

class tipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True, db_column='idTipop', verbose_name='ID_tipo_Producto')
    tipoProducto = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoProducto)
    
class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    tipoProducto = models.ForeignKey(tipoProducto, on_delete=models.CASCADE, db_column='idTipop')

    def __str__(self):
       return str(self.nombre)
    








