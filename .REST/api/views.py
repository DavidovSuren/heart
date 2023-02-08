
from .models import Event, Food
from rest_framework import viewsets, permissions
from .serializers import EventSerializer, FoodSerializer
from rest_framework import filters
from urllib import request

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    serializer_class = EventSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']

class FoodViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        category = self.request.query_params['category']
        if category :
            queryset = queryset.filter(category=category)
        return queryset
        return super().get_queryset()