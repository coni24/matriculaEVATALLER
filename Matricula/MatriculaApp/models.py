from django.db import models

class Estudiante(models.Model):
    RUT = models.CharField(max_length=9,unique=True)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    FechaNacimiento = models.DateField()
    Domicilio = models.CharField(max_length=20)
    Edad = models.IntegerField()
    Fono = models.CharField(max_length=9)

class Apoderado(models.Model):
    RUT = models.CharField(max_length=9,unique=True)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Fono = models.CharField(max_length=9)


class Matricula(models.Model):
    FechaMatricula= models.DateField()


class Trabajador(models.Model):
    NombreEmpleado = models.CharField()
    ApellidoEmpleado = models.CharField()


class EstadoMatricula(models.Model):
    Estado = models.CharField(max_length=15) #choices


class Parentesco(models.Model):
    Parentesco = models.CharField()

class Cargo(models.Model):
    Cargo = models.CharField()


class Perfil(models.Model):
    Perfil = models.CharField()


class Genero(models.Model):
    Genero = models.CharField() #choices


class Nacionalidad(models.Model):
    Nacionalidad = models.CharField()

#class NivelEducacional
