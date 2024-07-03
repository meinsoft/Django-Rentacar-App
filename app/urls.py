from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<slug:slug>/', views.car_detail, name='car_detail'), 
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]