from django.shortcuts import render, redirect
from .forms import EventForm
from accounts.models import NGOModel,VolunteerModel
from events.models import events,volunteer_event

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


def view_events(request):
    allevents =events.objects.all()
    print(events)
    context={
        'allevents':allevents
    }
    return render (request,'view_event.html',context)
def viewdetails(request):
    pass

def joinevent(request,pk):
    if request.user.role=="Volunteer":
        vid=request.user.id
        print(vid)
        Volunteer=VolunteerModel.objects.get(id=vid)
        Event=events.objects.get(pk=pk)
        entry=volunteer_event.objects.create(v_id=Volunteer,e_id=Event,hours=0)
        entry.save()


