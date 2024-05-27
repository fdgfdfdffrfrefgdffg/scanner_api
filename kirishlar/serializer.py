from rest_framework.serializers import ModelSerializer
from kirishlar.models import Kirish

class KirishSerializer(ModelSerializer):
    class Meta:
        model = Kirish
        fields = ["pk", "oquvchi_id", "sana", "vaqt"]
