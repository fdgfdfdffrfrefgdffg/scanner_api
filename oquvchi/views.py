from django.shortcuts import render
from oquvchi.models import Oquvchi
from oquvchi.serializer import OquvchiSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Oquvchi
from oquvchi.serializer import OquvchiSerializer
from facepplib import FacePP, exceptions
from oquvchi.serializer import LinkSerializer

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
    def post(self, request, *args, **kwargs):
        print("Test")
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            url_link = serializer.validated_data['url_link']
            rasm_file = url_link

            # Face++ API sozlamalari
            api_key = '_CR6B4vjRURT382BuHPZU4xlTCZ068Es'
            api_secret = 'DmWV0RfNXgBbLozKmrgTd3AcymKWHGqn'
            app_ = FacePP(api_key=api_key, api_secret=api_secret)
            res = {"topilganlar": []}
            # O'quvchilarni tekshirish
            for oquvchi in Oquvchi.objects.all():
                try:
                    # Face++ compare funksiyasini chaqirish
                    cmp_ = app_.compare.get(image_url1=rasm_file, image_url2=oquvchi.face_url)

                    # Agar yuzlar mos kelsa, o'quvchi ma'lumotlarini qaytarish
                    if cmp_.confidence > 70:
                        res["topilganlar"].append({
                            "ism_familya": oquvchi.ism_familya,
                            "sinf": oquvchi.sinf,
                            "maktab": oquvchi.maktab
                        })
    
                except exceptions.BaseFacePPError as e:
                    # Agar Face++ da xato bo'lsa, xato xabarini qaytarish
                    return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(res)
            # Agar hech qaysi yuz mos kelmasa, xabar qaytarish
            return Response({"message": "O'xshash yuz topilmadi."}, status=status.HTTP_404_NOT_FOUND)

    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    