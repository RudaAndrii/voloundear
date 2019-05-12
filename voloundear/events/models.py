from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Event(models.Model):
    CATEGORIES = (
        ('IT', 'IT'),
        ('Kids', 'Діти'),
        ('Concerts', 'Концерти'),
        ('Education', 'Освіта'),
    )

    CITIES = (
        ('Lviv', 'Львів'),
        ('Kyiv', 'Київ'),
        ('Kharkiv', 'Харків'),
        ('Dnipro', 'Дніпро'),
        ('Lugansk', 'Луганськ'),
    )

    topic = models.CharField(max_length=50, default='Event')
    category = models.CharField(max_length=15, choices=CATEGORIES)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    city = models.CharField(max_length=20, choices=CITIES)

    def __str__(self):
        return f'Event title: {self.topic}'


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return 'Points' + str(self.points)
