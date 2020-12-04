from django.contrib import admin
from .models import Libro, Profile
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display=['titulo', 'anio', 'paginas', 'pais', 'autor']
    search_fields=['titulo', 'anio', 'autor']
    list_filter=['anio']
    list_per_page=10

admin.site.register(Libro)
admin.site.register(Profile)