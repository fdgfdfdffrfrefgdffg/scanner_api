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
    path('kun/', views.kun, name='kun'),
    path('hafta/', views.hafta, name='hafta'),
    path('oy/', views.oy, name='oy'),
    path('yil/', views.yil, name='yil'),
]