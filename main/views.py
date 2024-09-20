from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def index(request):
  events = Event.objects.all()
  return render(request, 'index.html', {'events': events})

def event(request, id):
  event = Event.objects.get(id=id)
  return render(request, 'event.html', {'event': event})