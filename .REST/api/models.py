from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

FOOD_CHOICES = (
    ('c','Кафе'),
    ('r', 'Ресторан')
)

class Event(models.Model):
    title = models.CharField(max_length=250)
    img = models.FileField(upload_to='upload')
    description = models.TextField(max_length=10000)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Food(models.Model):
    title = models.CharField(max_length=250)
    img = models.FileField(upload_to='upload')
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
    #galery

    def __str__(self):
        return self.title
