# importing modules and sub-modules
from django import forms
from django.forms import ModelForm
from .models import Event

# Create your forms here.
class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = "__all__"

		labels = {
			"title": "",
			"location": "",
			"description": "",
			"date": "",
			"time": "",
			"tickets": "",
		}

		widgets = {
			"title": forms.TextInput(attrs={"placeholder":"Event Title", "class":"form-control", "style": "width:350px"}),
			"location": forms.TextInput(attrs={"placeholder":"Event Location", "class":"form-control", "style": "width:350px"}),
			"description": forms.Textarea(attrs={"placeholder":"Event Description", "class":"form-control", "style":"width:350px", "rows":"1"}),
			"date": forms.TextInput(attrs={"placeholder":"Event Date", "class":"form-control", "style": "width:350px"}),
			"time": forms.TextInput(attrs={"placeholder":"Event Time", "class":"form-control", "style": "width:350px"}),
			"tickets": forms.TextInput(attrs={"placeholder":"Event Ticket", "class":"form-control", "style": "width:350px"}),
		}
