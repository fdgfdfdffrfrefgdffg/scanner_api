from rest_framework.serializers import ModelSerializer
from oquvchi.models import Oquvchi
from rest_framework import serializers

class LinkSerializer(serializers.Serializer):
    url_link = serializers.URLField(max_length=200)

class OquvchiSerializer(ModelSerializer):
    class Meta:
        model = Oquvchi
        fields = ["pk", "ism_familya", "sinf", "maktab", "face_url"]
