from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=255, unique=True)
    stock = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    components = models.ManyToManyField(
        Component, 
        through="ProductComponent",
        related_name="products",
    )

    def __str__(self):
        return self.name

    def get_available_quantity(self):
        quantities = []

        for pc in self.product_components.all():
            stock = pc.component.stock
            required = pc.quantity

            possible = stock // required
            quantities.append(possible)

        if not quantities:
            return 0
        
        return min(quantities)

    def produce(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        
        components = self.product_components.all()

        if not components:
            raise ValueError("Product has no components")

        for pc in components:
            needed = quantity * pc.quantity
            if pc.component.stock < needed:
                raise ValueError(f"Not enough stock for {pc.component.name}" )

        for pc in components:
            needed = quantity * pc.quantity
            pc.component.stock -= needed
            pc.component.save()
            StockMovement.objects.create(component=pc.component, quantity=needed, type='production')

        
    



class ProductComponent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_components",)
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name="component_products",)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product} - {self.component} ({self.quantity})"

    class Meta:
        unique_together = ("product", "component")


class StockMovement(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='component_movements')
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.component} | {self.quantity} | {self.type}"