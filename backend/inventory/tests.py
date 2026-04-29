from django.test import TestCase
from django.db import IntegrityError

from .models import Component, Product, ProductComponent


class ProductTest(TestCase):
    def test_product_without_components_returns_zero(self):
        product = Product.objects.create(name="But")
        self.assertEqual(product.get_available_quantity(), 0)

    def test_return_minimum(self):
        product = Product.objects.create(name="But")
        c1 = Component.objects.create(name="podeszwa", stock=10)
        c2 = Component.objects.create(name="sznurówka", stock=20)
        ProductComponent.objects.create(product=product, component=c1, quantity=1)
        ProductComponent.objects.create(product=product, component=c2, quantity=2)
        
        self.assertEqual(product.get_available_quantity(), 10)

    
# Create your tests here.
