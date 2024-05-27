from django.urls import path
from oquvchi.views import AddOrGet, UpdateOrDel, GetMaktab, GetMaktabAndSinf, FaceCompareView

urlpatterns = [
    path("", AddOrGet.as_view(), name="Oquvchi qo'shish yoki hammasini olish"),
path('/<int:pk>/', UpdateOrDel.as_view(), name='update_or_delete'),
path('/maktab/<int:maktab>/', GetMaktab.as_view(), name="Maktab o'quvchilari"),
path('/maktab/<int:maktab>/<str:sinf>', GetMaktabAndSinf.as_view(), name="Maktab o'quvchilari"),
path("/check/", FaceCompareView.as_view(), name="Yuzlarni tekshirish")
]
