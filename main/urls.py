from django.urls import path
from . import views

urlpatterns = [
    path('',          views.home,     name='home'),
    path('services/', views.services, name='services'),
    path('about/',    views.about,    name='about'),
    path('contact/',  views.contact,  name='contact'),
    path('orders/', views.orders, name='orders'),
    path('api/orders/', views.orders_list, name='orders_list'),
    path('api/orders/save/', views.orders_save, name='orders_save'),
    path('api/orders/<int:order_id>/delete/', views.orders_delete, name='orders_delete'),
    path('api/orders/<int:order_id>/status/', views.orders_status, name='orders_status'),
    path('orders/login/',  views.orders_login,  name='orders_login'),
    path('orders/logout/', views.orders_logout, name='orders_logout'),
    path('quote/', views.quote, name='quote'),
]
