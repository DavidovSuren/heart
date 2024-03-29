from rest_framework import serializers
from .models import Event, Food, FoodGalery, Point, PointGalery

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodGalery
        fields = '__all__'
        extra_kwargs = {'photo': {'use_url' : True}}

class FoodSerializer(serializers.ModelSerializer):
    photos = GalerySerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = ["id","title","img","description","address","phone","menu","video","count","rating","openHour","closeHour","workPeriod","category","photos"]
        extra_kwargs = {'img': {'use_url' : True}}


class GaleryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointGalery
        fields = '__all__'
        extra_kwargs = {'photo': {'use_url' : True}}

class PointSerializer(serializers.ModelSerializer):
    photos = GaleryPointSerializer(many=True, read_only=True)

    class Meta:
        model = Point
        fields = ["id","title","img","description","address","menu","video","rating","openHour","closeHour","workPeriod","category","photos"]
        extra_kwargs = {'img': {'use_url' : True}}