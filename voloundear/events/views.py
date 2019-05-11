from django.shortcuts import render
from .models import Event
from django.http import HttpResponse


# Create your views here.
def main_view(request):
    if request.method == 'GET':
        events = Event.objects.all()
    elif request.method == 'POST':
        category = request.POST['category']
        events = Event.objects.filter(category=category)
    return render(request, 'events/main.html', {
        'events': events
    })


def post_event(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        content = request.POST['content']
        category = request.POST['category']
        new_event = Event(topic=topic, content=content, category=category)
        new_event.save()
        return HttpResponse('Event saved!')
    return render(request, 'events/add.html')
