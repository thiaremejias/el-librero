from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TIPO_VIVIENDA = (
('Casa con patio grande', 'Casa con patio grande'),
('Casa con patio pequeño', 'Casa con patio pequeño'),
('Casa sin patio', 'Casa sin patio'),
('Departamento', 'Departamento')
)

# clase para registrar clientes 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=12)
    fecha_nac = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=15)
    region = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    vivienda = models.CharField(max_length=100, choices=TIPO_VIVIENDA)
    
    def __str__(self):
        return self.user.username

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField(verbose_name="año")
    paginas = models.IntegerField()
    pais = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    sinopsis = models.TextField(null=True, blank=True)
    #fecha_estreno=models.DateField()
    imagen = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    