from django.urls import path
from maktab.views import AddOrGet, UpdateOrDel

urlpatterns = [
    path("", AddOrGet.as_view(), name="Oquvchi qo'shish yoki hammasini olish"),
    path('/<int:pk>/', UpdateOrDel.as_view(), name='update_or_delete'),
]
