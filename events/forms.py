from django import forms
from .models import events

class EventForm(forms.ModelForm):
    class Meta:
        model = events
        fields = '__all__'