from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home' ),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('products/', views.products, name = 'products'),
    path('create_order/', views.create_order, name = 'create_order'),
    path('update_order/<str:order_pk>/', views.update_order, name = 'update_order'),
    path('delete_order/<str:order_pk>/', views.delete_order, name = 'delete_order'),
    ]