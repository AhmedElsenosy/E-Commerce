from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.sign_up, name='register'),
    path('userinfo/', views.current_user , name='userinfo')
]
