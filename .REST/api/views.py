
from .models import Event, Food
from rest_framework import viewsets, permissions
from .serializers import EventSerializer, FoodSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    serializer_class = EventSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    serializer_class = FoodSerializer