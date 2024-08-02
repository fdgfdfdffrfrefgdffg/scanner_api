from django.urls import path
from Teleusers.views import AddOrGet, UpdateOrDel, GetOquvchiIdTeleusers

urlpatterns = [
    path("", AddOrGet.as_view(), name="Oquvchi qo'shish yoki hammasini olish"),
    path('<int:pk>/', UpdateOrDel.as_view(), name='update_or_delete'),
    path('oquvchi_id/<int:oquvchi_id>/', GetOquvchiIdTeleusers.as_view(), name="O'quvchi mavzusi"),
]

