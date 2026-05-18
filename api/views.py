from django.shortcuts import render
from rest_framework import generics
 
from api.model import Room
from api.serializers import RoomSerializer

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

