from django.db import models

class Importacion(models.Model):
    nombre_articulo = models.CharField(max_length=100)
    cantidad_unidades = models.PositiveIntegerField()
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_articulo = models.PositiveIntegerField()
    proveedor = models.CharField(max_length=100, default="Proveedor Desconocido")
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Resultado(models.Model):
    importacion = models.OneToOneField(Importacion, on_delete=models.CASCADE) #Relación OneToOne indica que hay una relación uno a uno entre dos modelos.    
    total_pedido = models.IntegerField()
    costo_envio = models.IntegerField()
    tasa_aduana = models.IntegerField()
    iva = models.IntegerField()
    total_impuestos = models.IntegerField()
    total_compra_clp = models.IntegerField()
    total_compra_usd = models.DecimalField(max_digits=10, decimal_places=2)
