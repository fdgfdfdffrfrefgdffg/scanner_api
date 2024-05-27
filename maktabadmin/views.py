from django.shortcuts import render
from maktabadmin.models import Admin
from maktabadmin.serializer import AdminSerializer
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
# Create your views here.

class AddOrGet(ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class UpdateOrDel(RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer