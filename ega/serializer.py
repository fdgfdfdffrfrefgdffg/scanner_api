from rest_framework.serializers import ModelSerializer
from ega.models import Ega

class EgaSerializer(ModelSerializer):
    class Meta:
        model = Ega
        fields = ["pk", "login", "parol", "ism_familya"]
