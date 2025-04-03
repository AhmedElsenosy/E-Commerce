from django.urls import path
from . import views 

urlpatterns = [
    path('products/' , views.get_all_products , name='products'),
    path('products/<str:pk>/' , views.get_by_id_products , name='get_by_id'),
    path('products/new' , views.add_product , name='new_product'),
    path('products/update/<str:pk>/' , views.update_product , name='update_product'),
    path('products/delete/<str:pk>/' , views.delete_product , name='delete_product'),
    path('<str:pk>/reviews' , views.add_review , name='add_review'),
    path('<str:pk>/reviews/delete' , views.delete_review , name='delete_review'),
]
