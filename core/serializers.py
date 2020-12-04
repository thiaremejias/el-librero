#serializador en django:
#entrega los datos desde la bd en formato JSON
# bbdd -> datos -> JSON
# y viceversa
# JSON -> datos -> bbdd

from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields=['titulo', 'anio', 'duracion', 'pais', 'director', 'sinopsis']