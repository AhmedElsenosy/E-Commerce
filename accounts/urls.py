from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.sign_up, name='register'),
    path('userinfo/', views.current_user , name='userinfo'),
    path('userinfo/update/', views.update_user , name='update_user'),
]
