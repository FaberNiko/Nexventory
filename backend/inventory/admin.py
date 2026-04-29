from django.contrib import admin
from .models import Component, Product, ProductComponent

admin.site.register(Component)
admin.site.register(Product)
admin.site.register(ProductComponent)   

# Register your models here.
