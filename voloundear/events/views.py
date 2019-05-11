from django.shortcuts import render
from .models import Event


# Create your views here.
def main_view(request):
    events = Event.objects.all()
