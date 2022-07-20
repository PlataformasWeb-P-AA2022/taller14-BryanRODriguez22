from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30, unique=True)
    tipo_opciones = (('Ecuatoriana', 'Ecuatoriana'), ('Peruana', 'Peruana'),('Colombiana', 'Colombiana'))
    nacionalidad = models.CharField(max_length=50, choices= tipo_opciones)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costo_depa = models.DecimalField(max_digits=5 ,decimal_places=2)
    num_cuartos = models.IntegerField()
    num_banio = models.IntegerField()
    alicuota = models.DecimalField(max_digits=5 ,decimal_places=2)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %s %s %s %s" % (self.costo_depa, 
                          self.num_cuartos,
                          self.num_banio,
                          self.alicuota,
                          self.propietario)
