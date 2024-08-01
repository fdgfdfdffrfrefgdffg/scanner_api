from rest_framework.serializers import ModelSerializer
from telegroups.models import Telegroup

class TelegroupSerializer(ModelSerializer):
    class Meta:
        model = Telegroup
        fields = "__all__"

