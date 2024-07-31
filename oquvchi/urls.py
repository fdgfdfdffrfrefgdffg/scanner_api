from django.urls import path
from oquvchi.views import AddOrGet, UpdateOrDel, GetMaktab, GetMaktabAndSinf, GetOquvchiData, GetOquvchiImg

urlpatterns = [
    path("", AddOrGet.as_view(), name="Oquvchi qo'shish yoki hammasini olish"),
    path("data/", GetOquvchiData.as_view(), name="Oquvchi ma'lumotlari"),
    path("img/", GetOquvchiImg.as_view(), name="Oquvchi rasmlari"),
    path('<int:pk>/', UpdateOrDel.as_view(), name='update_or_delete'),
    path('maktab/<int:maktab>/', GetMaktab.as_view(), name="Maktab o'quvchilari"),
    path('maktab/<int:maktab>/<str:sinf>', GetMaktabAndSinf.as_view(), name="Maktab o'quvchilari"),
]
