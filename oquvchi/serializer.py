from rest_framework.serializers import ModelSerializer
from oquvchi.models import Oquvchi
from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    rasm = serializers.ImageField(use_url=True)

class OquvchiSerializer(ModelSerializer):
    class Meta:
        model = Oquvchi
        fields = "__all__"

class OquvchiDataSerializer(ModelSerializer):
    class Meta:
        model = Oquvchi
        fields = ["pk", "ism_familya", "sinf", "maktab", "phone", "manzil"]

class OquvchiImgSerializer(ModelSerializer):
    class Meta:
        model = Oquvchi
        fields = ["pk", "face_data", "face_img"]

