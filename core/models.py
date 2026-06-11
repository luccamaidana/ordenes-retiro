from django.db import models

# Create your models here.
class OrdenPedido(models.Model):
    id_solicitante = models.CharField(max_length=30)
    tipo_servicio = models.CharField(max_length=50)
    
    # 1. Definimos las opciones del estado
    class EstadoChoices(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        ACTIVO = 'ACTIVO', 'Activo'
        CANCELADO = 'CANCELADO', 'Cancelado'
    
    # 2. El campo real de la base de datos que usa esas opciones
    estado = models.CharField(
        max_length=9,
        choices=EstadoChoices.choices,
        default=EstadoChoices.PENDIENTE
    )
    # El validator funciona con Django Forms, por lo que no validaremos en Models, sino en Views
   ## cantidad_bulto = models.IntegerField(
     ##   validators=MinValueValidator(1, message = "La cantida de bultos debe ser mayor a 0")
       ## )
    cantidad_bulto = models.IntegerField()

    # 3. Observación suele requerir null/blank por si no quieren escribir nada
    observacion = models.CharField(max_length=100, blank=True, null=True)

