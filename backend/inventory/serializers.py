from rest_framework import serializers

from inventory.models import Product, Component

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'stock']
