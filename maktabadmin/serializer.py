from rest_framework.serializers import ModelSerializer
from maktabadmin.models import Admin

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = ["pk", "login", "parol", "ism_familya", "maktab"]
