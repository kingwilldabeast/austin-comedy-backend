from django.shortcuts import render

from rest_framework import generics
from .serializers import OpenMicSerializer
from .models import open_mic

# Create your views here.
class OpenMicList(generics.ListCreateAPIView):
    queryset = open_mic.objects.all()
    serializer_class = OpenMicSerializer

class OpenMicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = open_mic.objects.all()
    serializer_class = OpenMicSerializer

