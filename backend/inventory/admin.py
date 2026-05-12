from django.contrib import admin
from .models import Component, Product, ProductComponent, StockMovement

admin.site.register(Component)
admin.site.register(Product)
admin.site.register(ProductComponent)   
admin.site.register(StockMovement)
# Register your models here.
