from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def _str_(self):
        return f'{self.rut} - {self.apellido}, {self.nombre}'


class Profesor(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def _str_(self):
        return f'{self.rut} - {self.apellido}, {self.nombre}'


class Direccion(models.Model):
    calle = models.CharField(max_length=50, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, blank=False, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, blank=False, null=False)
    estudiante_id = models.OneToOneField(Estudiante, on_delete=models.CASCADE, null=False, unique=True)

    def _str_(self):
        return f'{self.Estudiante_id} - {self.calle} - {self.dpto} - {self.comuna} - {self.ciudad} - {self.region}'


class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    version = models.IntegerField()
    profesor_id = models.ManyToManyField(Profesor)
    estudiante_id = models.ManyToManyField(Estudiante)

    def _str_(self):
        return f'{self.codigo} - {self.nombre}, v:{self.version}'

