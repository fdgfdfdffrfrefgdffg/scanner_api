from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from telegroups.models import Telegroup
from telegroups.serializers import TelegroupSerializer
# Create your views here.

class AddOrGet(ListCreateAPIView):
    queryset = Telegroup.objects.all()
    serializer_class = TelegroupSerializer

class UpdateOrDel(RetrieveUpdateDestroyAPIView):
    queryset = Telegroup.objects.all()
    serializer_class = TelegroupSerializer

class GetClassTelegroups(ListAPIView):
    queryset = Telegroup.objects.all()
    serializer_class = TelegroupSerializer

    def get_queryset(self):
        sinf = self.kwargs.get('sinf')
        return Telegroup.objects.filter(sinf=sinf)

    lookup_field = "sinf"

class GetOquvchiIdTelegroups(ListAPIView):
    queryset = Telegroup.objects.all()
    serializer_class = TelegroupSerializer

    def get_queryset(self):
        oquvchi_id = self.kwargs.get('oquvchi_id')
        return Telegroup.objects.filter(oquvchi_id=oquvchi_id)

    lookup_field = "oquvchi_id"

