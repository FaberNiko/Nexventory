from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from inventory.models import Product
from inventory.serializers import ProductSerializer


@api_view(["GET", "POST"])
def products_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
# Create your views here.
