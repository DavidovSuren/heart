
from .models import Event, Food
from rest_framework import filters, viewsets, permissions
from .serializers import EventSerializer, FoodSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    serializer_class = EventSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']