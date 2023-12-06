from django.db import models

# Create your models here.
class tiendaInfo(models.Model):
    direccionTienda = models.CharField(max_length=32, blank=True, null=True)
    provinciaTienda = models.CharField(max_length=32, blank=True, null=True)
    regionTienda = models.CharField(max_length=32, blank=True, null=True)
    fechaCreacionTienda = models.CharField(max_length=32, blank=True, null=True)
    telefonoContactoTienda = models.CharField(max_length=32, blank=True, null=True)

class productoInfo(models.Model):
    descripcionProducto = models.CharField(max_length=100, blank=True, null=True)
    codigoProducto = models.CharField(max_length=32, blank=True, null=True)
    pvProducto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidadProducto = models.IntegerField()    
    tiendaRelacionado = models.ForeignKey(tiendaInfo, blank=True, null=True, on_delete=models.SET_NULL)  