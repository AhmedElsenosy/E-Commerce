from django.shortcuts import render , get_object_or_404 
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import *
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated 


# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    page = 4
    paginator = PageNumberPagination()
    paginator.page_size = page

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = ProductSerializer( queryset , many = True)
    return Response({"products":serializer.data , "Count":count})

@api_view(['GET'])
def get_by_id_products(request , pk):
    product = get_object_or_404(Product , id = pk)
    serializer = ProductSerializer(product , many = False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        product = Product.objects.create(**data , user=request.user)
        new_product = ProductSerializer(product , many = False)
        return Response({"product":new_product.data})
    
    else:
        return Response({"error":serializer.errors})
        
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request , pk):
    product = get_object_or_404(Product , id = pk)
    
    if product.user != request.user:
        return Response({"error":"Sorry you are not allowed to update this product"}
                        , status=status.HTTP_403_FORBIDDEN)

    product.name = request.data['name'] 
    product.description = request.data['description'] 
    product.price = request.data['price'] 
    product.brand = request.data['brand'] 
    product.category = request.data['category'] 
    product.rating = request.data['rating'] 
    product.stock = request.data['stock'] 

    product.save()
    serializer = ProductSerializer(product , many = False)

    return Response({"product":serializer.data})
    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request , pk):
    product = get_object_or_404(Product , id = pk)
    
    if product.user != request.user:
        return Response({"error":"Sorry you are not allowed to delete this product"}
                        , status=status.HTTP_403_FORBIDDEN)



    product.delete()

    return Response({"message":"Product deleted successfully"} , status=status.HTTP_200_OK)
    


