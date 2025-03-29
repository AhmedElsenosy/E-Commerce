from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import *
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    page = 2
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