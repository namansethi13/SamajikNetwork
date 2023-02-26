from django.shortcuts import render, redirect
from .forms import EventForm
from accounts.models import NGOModel,VolunteerModel
from events.models import events,volunteer_event
from django.db.models import Q

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
    if(request.user.is_authenticated):
        VolunteerInstance = VolunteerModel.objects.get(username=request.user.username)
        joined_events = volunteer_event.objects.filter(v_id = VolunteerInstance )
        e_id_list = []
        for e in joined_events:
            e_id_list += [e.e_id.e_id]
        allevents =events.objects.all()
        context={
        'allevents':allevents,
        'joinedevents': e_id_list
        }
        print(context['allevents'])      
        print(context['joinedevents'])
        return render (request,'view_events.html',context)
    else:
        return redirect('login')
def viewdetails(request):
    pass

def join_event(request,e_id):
    if request.user.role=="VOLUNTEER":
        vid=request.user.id
        Volunteer=VolunteerModel.objects.get(id=vid)
        Event=events.objects.get(pk=e_id)
        entry=volunteer_event.objects.create(v_id=Volunteer,e_id=Event,hours=0)
        entry.save()
        VolunteerInstance = VolunteerModel.objects.get(username=request.user.username)
        joined_events = volunteer_event.objects.filter(v_id = VolunteerInstance )
        allevents =events.objects.all()
        e_id_list = []
        for e in joined_events:
            e_id_list += [e.e_id.e_id]
        allevents =events.objects.all()
        context={
        'allevents':allevents,
        'joinedevents': e_id_list
        }   
    return render (request,'view_events.html',context)

def delete (request ,e_id=0):
    print(id)
    if id:
        try:
            remove=events.objects.get(pk =e_id)
            remove.delete()
            print('deleted event')
            return redirect('dashboard')
        except:
            print('unable to delete ')
