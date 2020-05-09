from django.db import models

# Create your models here.
class User(models.Model):
    """ Define la tabla User """
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),
        ("M", "Mujer"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)
    clave = models.CharField(max_length=40, null=True, blank=True)
    tipo = models.CharField(max_length=45, null=True, blank=True)

class Zona(models.Model):
    """ Define la tabla Zona """
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=45)
    latitud = models.DecimalField(max_digits=19, decimal_places=10)
    longitud = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.nombre

class Tour(models.Model):
    """ Define la tabla Tour """
    nombre = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operador = models.CharField(max_length=45, null=True, blank=True)
    tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=256)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_llegada")

    def __str__(self):
        return "{}".format(self.nombre)