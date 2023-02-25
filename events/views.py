from django.shortcuts import render, redirect
from .forms import EventForm

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})