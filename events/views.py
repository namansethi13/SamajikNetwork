from django.shortcuts import render, redirect
from .forms import EventForm
from accounts.models import NGOModel
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is  valid")
            event = form.save(commit=False)
            ngoInstance = NGOModel.objects.get(username=request.user.username)
            event.ngo_id = ngoInstance
            event.save()
            return redirect('/')
        else:
            print("form is not valid")
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})