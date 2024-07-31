from rest_framework.serializers import ModelSerializer
from chiqish.models import Chiqish

class ChiqishSerializer(ModelSerializer):
    class Meta:
        model = Chiqish
        fields = ["pk", "oquvchi_id", "sana", "vaqt"]

