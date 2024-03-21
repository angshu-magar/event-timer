from django.shortcuts import get_object_or_404, redirect, render
from .models import Event
from .forms import EventForm
from django.utils import timezone

# Create your views here.

def index_view(request):
    upcoming = Event.objects.filter(date__gt=timezone.now()).order_by('date')
    completed = Event.objects.filter(date__lte=timezone.now()).order_by('-date')
    context = {
        'completed_event_list' : completed,
        'upcoming_event_list' : upcoming,
    }
    return render(request, 'index.html', context)

def create_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        form.save()
        return redirect('index_view')

    form = EventForm()
    title = "Create"
    context = {
        'form' : form,
        'title' : title,
    }
    return render(request, 'edit_event.html', context)

def update_view(request, event_pk):
    event = get_object_or_404(Event, id=event_pk)
    form = EventForm(instance=event)
    title = "Update"

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        form.save()
        return redirect('index_view')

    context = {
        'form' : form,
        'title' : title,
    }
    return render(request, 'edit_event.html', context)

def delete_view(request, event_pk):
    event = get_object_or_404(Event, id=event_pk)
    if request.method == 'POST':
        event.delete()
        return redirect('index_view')
    context = {
        'event' : event,
    }
    return render(request, 'delete_event.html', context)

def timer_view(request, event_pk):
    event = get_object_or_404(Event, id=event_pk)
    context = {
        'event' : event,
    }
    return render(request, 'timer.html', context)
