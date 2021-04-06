from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from core.models import BaseModel
from crum import get_current_user
# Create your models here.
class Clientes(BaseModel):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    nro_documento = models.CharField(max_length=10, unique=True, verbose_name='C.I')
    nro_telefono = models.CharField(max_length=10, verbose_name='Nro. Telefono', null=True, blank=True)
    direccion = models.CharField(max_length=150, verbose_name='Direccion', null=True, blank=True)

    def __str__(self):
        return self.nombres

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Clientes, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clientes'
        ordering = ['id']

class Prestamos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name='Cod. Cliente')
    idprestamo = models.PositiveIntegerField(default=0, verbose_name='Cod. Prestamo')
    fechaprestamo = models.DateField(default=datetime.now, verbose_name='Fecha Prestamo')
    producto = models.CharField(max_length=150, verbose_name='Producto')
    interes = models.PositiveIntegerField(default=0, verbose_name='Interes')
    montototal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Total')
    observaciones = models.CharField(max_length=150, verbose_name='Observaciones', null=True, blank=True)
    fechavencimiento = models.DateField(default=datetime.now, verbose_name='Fecha Vencimiento', null=True, blank=True)
    estado = models.CharField(max_length=15, verbose_name='Estado', null=True, blank=True)

    def __str__(self):
        return self.producto

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table = 'prestamos'
        ordering = ['id']

class Caja(models.Model):
    montoingreso = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Ingresos', null=True, blank=True)
    montoegreso = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Egresos', null=True, blank=True)
    fechamovimiento = models.DateField(default=datetime.now, verbose_name='Fecha Movimiento')
    motivoaccion = models.CharField(max_length=150, verbose_name='Motivo')
    operacion = models.CharField(max_length=10, verbose_name='Operación')

    def __str__(self):
        return self.motivoaccion

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'
        db_table = 'caja'
        ordering = ['id']

class Pagos(models.Model):
    codprestamo = models.ForeignKey(Prestamos, on_delete=models.CASCADE, verbose_name='Cod. Prestamo')
    nombrerecibo = models.CharField(max_length=50, verbose_name='Nombre')
    fechapago = models.DateField(default=datetime.now, verbose_name='Fecha de Pago')
    montopago = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Pagado')

    def __str__(self):
        return self.nombrerecibo

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        db_table = 'pagos'
        ordering = ['id']


class Compras(models.Model):
    nombrecompleto = models.CharField(max_length=100, verbose_name='Nombre Completo')
    nro_documento = models.CharField(max_length=10, verbose_name='C.I', null=True, blank=True)
    nro_telefono = models.CharField(max_length=10, verbose_name='Nro. Telefono', null=True, blank=True)
    fechacompra = models.DateField(default=datetime.now, verbose_name='Fecha de Compra')
    producto = models.CharField(max_length=150, verbose_name='Producto')
    montocompra = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Compra')
    observaciones = models.CharField(max_length=150, null=True, blank=True, verbose_name='Observaciones')
    estado = models.CharField(max_length=15, verbose_name='Estado', null=True, blank=True)
 
    def __str__(self):
        return self.nombrecompleto

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'compras'
        ordering = ['id']

class Entregados(models.Model):
    codprestamo = models.ForeignKey(Prestamos, on_delete=models.CASCADE, verbose_name='Cod. Prestamo')
    fechaprestamo = models.DateField(default=datetime.now, verbose_name='Fecha de Prestamo')
    fechaentrega = models.DateField(default=datetime.now, verbose_name='Fecha de Entrega')
    montoprestamo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Prestado')
    interes = models.PositiveIntegerField(default=0, verbose_name='Interes')
    montoapagar = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto a Pagar')
    montopagado = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Pagado')
 
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Entregado'
        verbose_name_plural = 'Entregados'
        db_table = 'entregados'
        ordering = ['id']


class Vendidos(models.Model):
    codarticulo = models.ForeignKey(Compras, on_delete=models.CASCADE, verbose_name='Cod. Artículo')
    fechaventa = models.DateField(default=datetime.now, verbose_name='Fecha de Venta')
    nombrecomprador = models.CharField(max_length=100, verbose_name='Nombre del Comprador')
    montoventa = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto Vendido')
    producto = models.CharField(max_length=150, verbose_name='Producto')
    observaciones = models.CharField(max_length=150, null=True, blank=True, verbose_name='Observaciones')
    tipoarticulo = models.CharField(max_length=10, null=True, blank=True, verbose_name='Tipo de Artículo')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Vendido'
        verbose_name_plural = 'Vendidos'
        db_table = 'vendidos'
        ordering = ['id']
