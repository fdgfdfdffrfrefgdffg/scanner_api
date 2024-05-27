from rest_framework.serializers import ModelSerializer
from maktab.models import Maktab

class MaktabSerializer(ModelSerializer):
    class Meta:
        model = Maktab
        fields = ["pk", "Maktab_raqami"]
