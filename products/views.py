from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from rest_framework.authentication import BaseAuthentication
#from rest_framework.permissions import IsAuthenticated

#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.authtoken.models import Token



from .serializers import ProductSerializer
from .models import Product

# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response( {"status": "success", "data": serializer.data},status="200")


@api_view(['GET'])
def ViewProduct(request,pk):   
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['POST'])
def UpdateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def DeleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Products delete successfully!')