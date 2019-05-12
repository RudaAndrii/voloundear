from django.shortcuts import render, redirect
from .models import Event, UserProfile
from django.http import HttpResponse


# Create your views here.
def main_view(request):
    if request.method == 'GET':
        events = Event.objects.all()
    elif request.method == 'POST':
        category = request.POST['category']
        events = Event.objects.filter(category=category)
    return render(request, 'events/welfare/index.html', {
        'events': events
    })


def post_event(request):
    if request.method == 'POST':
        city = request.POST['event-city']
        category = request.POST['event-category']
        topic = request.POST['event-topic']
        content = request.POST['event-content']

        new_event = Event(city=city, category=category, topic=topic, content=content)
        new_event.save()
        return redirect('main-events')
    return render(request, 'events/welfare/create.html')
