from django.db import models
from django.contrib.auth.models import User


# 1. Categoria (Ya la tenías)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


# 2. Producto (NUEVO)
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    # Relación 1:N con Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="productos")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre} ({self.stock} unid.)"


# 3. Cliente (NUEVO - Extiende User)
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField()

    def __str__(self):
        return self.usuario.username


# 4. Pedido (NUEVO - Cabecera)
class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PEN', 'Pendiente'
        ENVIADO = 'ENV', 'Enviado'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=3, choices=Estado.choices, default=Estado.PENDIENTE)

    # Relación N:M a través de tabla intermedia
    productos = models.ManyToManyField(Producto, through='DetallePedido')

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente}"


# 5. DetallePedido (NUEVO - Tabla intermedia explícita)
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # Evitar duplicados del mismo producto en el mismo pedido
        constraints = [
            models.UniqueConstraint(fields=['pedido', 'producto'], name='unique_producto_pedido')
        ]