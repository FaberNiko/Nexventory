from rest_framework import serializers

from inventory.models import Product, Component, StockMovement

class ProductSerializer(serializers.ModelSerializer):
    available_quantity = serializers.SerializerMethodField()
    def get_available_quantity(self, obj):
        return obj.get_available_quantity()
    class Meta:
        model = Product
        fields = ['id', 'name', 'available_quantity']

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'stock']

class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = ['id', 'component', 'quantity', 'type', 'created_at']