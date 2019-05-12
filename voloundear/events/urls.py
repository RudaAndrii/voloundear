from django.urls import path
from . import views as event_views

urlpatterns = [
    path('', event_views.main_view, name='main-events'),
    path('create/', event_views.post_event, name='create-event'),
]
