from rest_framework import serializers
from .models import Event, Food, FoodGalery

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        extra_kwargs = {‘img’: {‘use_url’: True}}


class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodGalery
        fields = '__all__'
        extra_kwargs = {‘photo’: {‘use_url’: True}}
