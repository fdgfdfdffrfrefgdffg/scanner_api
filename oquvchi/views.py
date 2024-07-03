from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.files.base import ContentFile
import os
from django.core.files.storage import default_storage
from kirishlar.models import Kirish
from datetime import datetime, date
from time import time
import requests
from oquvchi.models import Oquvchi
from oquvchi.serializer import OquvchiSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Oquvchi
from facepplib import FacePP, exceptions
from oquvchi.serializer import ImageUploadSerializer

class AddOrGet(ListCreateAPIView):
    queryset = Oquvchi.objects.all()
    serializer_class = OquvchiSerializer

class UpdateOrDel(RetrieveUpdateDestroyAPIView):
    queryset = Oquvchi.objects.all()
    serializer_class = OquvchiSerializer

class GetMaktab(ListAPIView):
    queryset = Oquvchi.objects.all()
    serializer_class = OquvchiSerializer

    def get_queryset(self):
        maktab = self.kwargs.get('maktab')
        return Kirish.objects.filter(oquvchi_id=maktab)

    lookup_field = "maktab"

class GetMaktabAndSinf(ListAPIView):
    queryset = Oquvchi.objects.all()
    serializer_class = OquvchiSerializer
    lookup_field = ["maktab", "sinf"]

    def get_queryset(self):
        maktab = self.kwargs.get('maktab')
        sinf = self.kwargs.get('sinf')
        return Kirish.objects.filter(oquvchi_id=maktab, sinf=sinf)