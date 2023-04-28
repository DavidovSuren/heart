from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

FOOD_CHOICES = (
    ('c','Кафе'),
    ('r', 'Ресторан')
)
POINT_CHOICES = (
    ('f','Пешком'),
    ('a', 'Авто'),
    ('b','Вело'),
    ('g','Гид')
)
class Event(models.Model):
    title = models.CharField(max_length=250)
    img = models.FileField(upload_to='static/upload')
    description = models.TextField(max_length=10000)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Food(models.Model):
    title = models.CharField(max_length=250)
    img = models.FileField(upload_to='static/upload')
    description = models.TextField(max_length=10000)
    address = models.CharField(max_length=500)
    menu = models.CharField(max_length=500, blank=True)
    video = models.CharField(max_length=500, blank=True)
    rating = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    open = models.IntegerField(
        default=9,
        validators=[
            MaxValueValidator(24),
            MinValueValidator(0)
        ]
    )
    close = models.IntegerField(
        default=18,
        validators=[
            MaxValueValidator(24),
            MinValueValidator(0)
        ]
    )
    category = models.CharField(max_length=1, choices=FOOD_CHOICES, default='с')

    def __str__(self):
        return self.title

class FoodGalery(models.Model):
    show = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to='static/upload')


class Point(models.Model):
    title = models.CharField(max_length=250)
    img = models.FileField(upload_to='static/upload')
    description = models.TextField(max_length=10000)
    address = models.CharField(max_length=500)
    menu = models.CharField(max_length=500, blank=True)
    video = models.CharField(max_length=500, blank=True)
    rating = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    open = models.IntegerField(
        default=9,
        validators=[
            MaxValueValidator(24),
            MinValueValidator(0)
        ]
    )
    close = models.IntegerField(
        default=18,
        validators=[
            MaxValueValidator(24),
            MinValueValidator(0)
        ]
    )
    category = models.CharField(max_length=1, choices=POINT_CHOICES, default='f')

    def __str__(self):
        return self.title

class PointGalery(models.Model):
    show = models.ForeignKey(
        Point, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to='static/upload')