from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('date/', views.date, name='date'),
    path('oquvchi/', views.oquvchi, name='oquvchi'),
    path('haqida/', views.haqida, name='haqida'),
    path('oquvchi/<int:id>/', views.haqida, name='haqida'),
    path('sinf/', views.sinf, name='sinf'),
    path('oquvchilar', views.oquvchilar, name='oquvchilar'),
]