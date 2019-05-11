from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Event(models.Model):
    CATEGORIES = (
        ('IT', 'IT'),
        ('Kids', 'Kids'),
        ('Concerts', 'Concerts'),
        ('Education', 'Education'),
    )

    topic = models.CharField(max_length=50, default='Event')
    category = models.CharField(max_length=15, choices=CATEGORIES)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Event title: {self.topic}'


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.points
