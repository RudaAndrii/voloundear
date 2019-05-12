from django.shortcuts import render
from .models import Event, UserProfile
from django.http import HttpResponse


# Create your views here.
def main_view(request):
    if request.method == 'GET':
        events = Event.objects.all()
    elif request.method == 'POST':
        category = request.POST['category']
        events = Event.objects.filter(category=category)
    return render(request, 'events/index.html', {
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


def leaderboard(request):
    user_profiles = UserProfile.objects.order_by('-points')
    return render(request, 'events/leaderboard.html', {
        'users': user_profiles
    })
