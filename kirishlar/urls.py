from django.urls import path
from kirishlar.views import AddOrGet, UpdateOrDel, GetSana, GetOquvchi, ExcelReportAPIView, KirishCreateView

urlpatterns = [
    path("", AddOrGet.as_view(), name="hammasini olish"),
    path("add/", KirishCreateView.as_view(), name="Qo'shish"),
    path("hisobot/<int:maktab>/<int:kun>", ExcelReportAPIView.as_view(), name="qo'shish yoki hammasini olish"),
    path('<int:pk>/', UpdateOrDel.as_view(), name='update_or_delete'),
    path('oquvchi/<int:oquvchi_id>/', GetOquvchi.as_view(), name='get oquvchi'),
    path('sana/<int:kun>', GetSana.as_view(), name='update_or_delete'),
]
