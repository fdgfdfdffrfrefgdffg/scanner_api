from django.shortcuts import render
from maktab.models import Maktab
from maktab.serializer import MaktabSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class AddOrGet(ListCreateAPIView):
    queryset = Maktab.objects.all()
    serializer_class = MaktabSerializer


class UpdateOrDel(RetrieveUpdateDestroyAPIView):
    queryset = Maktab.objects.all()
    serializer_class = MaktabSerializer

