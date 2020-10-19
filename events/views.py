from django.shortcuts import render
from .models import Event


def events(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events.html', context)


def event_details(request, pk):
    event = Event.objects.get(id=pk)
    context = {
        'event': event
    }
    return render(request, 'events/event_details.html', context)
