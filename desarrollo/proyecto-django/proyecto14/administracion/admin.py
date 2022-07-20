from distutils.debug import DEBUG
from django.contrib import admin

from administracion.models import *

# Register your models here.

class PropietarioAdmin(admin.ModelAdmin):
        list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
        search_fields = ('nombre', 'cedula', 'nacionalidad')
admin.site.register(Propietario, PropietarioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
        list_display = ('costo_depa', 'num_cuartos','num_banio','alicuota')
        raw_id_fields = ('propietario',) 
admin.site.register(Departamento, DepartamentoAdmin)