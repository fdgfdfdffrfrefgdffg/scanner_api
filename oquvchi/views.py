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

    lookup_field = "maktab"

class GetMaktabAndSinf(ListAPIView):
    queryset = Oquvchi.objects.all()
    serializer_class = OquvchiSerializer

    lookup_field = ["maktab", "sinf"]

class FaceCompareView(APIView):
    parser_classes = (FileUploadParser,)

    def get(self, request, *args, **kwargs):    
        return Response({"message": "Bu yerga faqat post qiling."})
    def post(self, request, *args, **kwargs):   
        try:
            if request.FILES["file"]:
            
                rasm = request.FILES["file"]
                img_path = f"media/{time()}{rasm.name}"
                
                with open(img_path, "wb") as f:
                    f.write(rasm.read())
                
                rasm_url = f"https://maktab-davomat.uz/" + img_path
                api_key = 'hRKyY_ca3CmuOl4BVYAFa1D1cETKckFT'
                api_secret = 'Tn0KO__Zes3bD_Nxpoqgs4L8Wwok7rax'
                app_ = FacePP(api_key=api_key, api_secret=api_secret)
                res = {"topilganlar": []}
                # O'quvchilarni tekshirish
                for oquvchi in Oquvchi.objects.all():
                    # try:
                        # Face++ compare funksiyasini chaqirish
                        cmp_ = app_.compare.get(image_url1=img_path, image_url2="https://maktab-davomat.uz/"+ oquvchi.face_url)


                        # Agar yuzlar mos kelsa, o'quvchi ma'lumotlarini qaytarish
                        if cmp_.confidence > 70:
                            res["topilganlar"].append({
                                "ism_familya": oquvchi.ism_familya,
                                "sinf": oquvchi.sinf,
                                "maktab": oquvchi.maktab,
                                "Telefon_raqam": oquvchi.phone,
                                "manzil": oquvchi.manzil,
                            })
            else:
                os.remove(img_path)
                return Response(res) if res else Response({"message": "O'xshash yuz topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
                # Agar Face++ da xato bo'lsa, xato xabarini qaytarish
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response({"Message": "Rasm yuborilmagan"}, status=status.HTTP_400_BAD_REQUEST)
            