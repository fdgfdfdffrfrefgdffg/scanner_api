from django.urls import path
from telegroups.views import AddOrGet, UpdateOrDel, GetClassTelegroups, GetOquvchiIdTelegroups

urlpatterns = [
    path("", AddOrGet.as_view(), name="Oquvchi qo'shish yoki hammasini olish"),
    path('<int:pk>/', UpdateOrDel.as_view(), name='update_or_delete'),
    path('sinf/<str:sinf>/', GetClassTelegroups.as_view(), name="Sinf guruhidagilar"),
    path('oquvchi_id/<int:oquvchi_id>/', GetOquvchiIdTelegroups.as_view(), name="O'quvchi mavzusi"),
]

