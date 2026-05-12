from django.test import TestCase
from django.db import IntegrityError

from .models import Component, Product, ProductComponent, StockMovement


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


    def test_produce_raises_when_quantity_is_non_positive(self):
        product = Product.objects.create(name="But")
        
        with self.assertRaises(ValueError):
            product.produce(0)

        with self.assertRaises(ValueError):
            product.produce(-1)

    def test_produce_decreases_stock(self):
         product = Product.objects.create(name="But")
         c1 = Component.objects.create(name="podeszwa", stock=10)
         c2 = Component.objects.create(name="sznurówka", stock=20)
         ProductComponent.objects.create(product=product, component=c1, quantity=1)
         ProductComponent.objects.create(product=product, component=c2, quantity=2)

         product.produce(3)

         c1.refresh_from_db()
         c2.refresh_from_db()
         self.assertEqual(c1.stock, 7)
         self.assertEqual(c2.stock, 14)

    def test_produce_creates_StockMovement(self):
         product = Product.objects.create(name="But")
         c1 = Component.objects.create(name="podeszwa", stock=10)
         ProductComponent.objects.create(product=product, component=c1, quantity=1)
         product.produce(3)
         movement = StockMovement.objects.first()

         self.assertEqual(StockMovement.objects.count(), 1)
         self.assertEqual(movement.type, 'production')
         self.assertEqual(movement.quantity, 3)
        
        


    
# Create your tests here.
