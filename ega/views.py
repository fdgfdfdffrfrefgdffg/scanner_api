from django.shortcuts import render
from ega.models import Ega
from ega.serializer import EgaSerializer
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
# Create your views here.

class AddOrGet(ListCreateAPIView):
    queryset = Ega.objects.all()
    serializer_class = EgaSerializer

class UpdateOrDel(RetrieveUpdateDestroyAPIView):
    queryset = Ega.objects.all()
    serializer_class = EgaSerializer