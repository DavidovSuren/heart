
from .models import Event, Food, FoodGalery, Point
from rest_framework import filters, viewsets, permissions
from .serializers import EventSerializer, FoodSerializer, GalerySerializer, PointSerializer
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

class PointsViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    serializer_class = PointSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

class GaleryViewSet(viewsets.ModelViewSet):
    queryset = FoodGalery.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    serializer_class = GalerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['show']