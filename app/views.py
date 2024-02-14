# importing modules and sub-modules
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event
from .forms import EventForm

# create your views here
# home/index page view
def index(request):
	return render(request, "index.html", {})

# creating event view
def create_event(request):
	form = EventForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			messages.success(request, "Event Created!")
			return redirect("index")

	return render(request, "create_event.html", {"form": form})

# reading event view
def read_event(request):
	event = Event.objects.all()
	return render(request, "read_event.html", {"event": event})

# updating event view
def update_event(request, id):
	events = Event.objects.get(pk=id)
	form = EventForm(request.POST or None, instance=events)
	if form.is_valid():
		form.save()
		messages.success(request, "Form Updated Successively!")
		return redirect("read_event")

	return render(request, "update_event.html", {"events": events, "form": form})

# delete event view
def delete_event(request, id):
	event = Event.objects.get(pk=id)
	event.delete()
	return redirect('index')