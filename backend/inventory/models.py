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

    



class ProductComponent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_components",)
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name="component_products",)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product} - {self.component} ({self.quantity})"

    class Meta:
        unique_together = ("product", "component")


