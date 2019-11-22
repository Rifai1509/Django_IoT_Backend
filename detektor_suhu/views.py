from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from detektor_suhu.models import stats
from detektor_suhu.serialrizers import StatsSerializers
class StatsViewSet (viewsets.ModelViewSet):
    queryset = stats.objects.all()
    serializer_class = StatsSerializers