from django.views.generic import CreateView, TemplateView
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from .models import NGOModel, VolunteerModel
from events.models import volunteer_event , events
from django.contrib.auth import logout
from .forms import SignUpForm
from .custom_decorators import logout_required
import logging
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .choices import RoleType, ShortRoleType
from django.contrib.auth import get_user_model
User = get_user_model()
all_user_events = {}
volunteers_of_events = {}
def ok(request):
    volunteers = VolunteerModel.objects.all()
    volunteer_events = volunteer_event.objects.all()
    # print(volunteer_events)
            # volunteer_events_A = volunteer_event.objects.filter(v_id=volunteer)
    for volunteer in volunteers:
        for v in volunteer_events:
            # print("in")
            if v.v_id == volunteer:
               all_user_events[volunteer] = []

    for volunteer in volunteers:
        for v in volunteer_events:
            # print("in")
            if v.v_id == volunteer:
               all_user_events[volunteer] += [v.e_id.e_id]
            # print(event_of_volunteer)

class SignUpView(CreateView):
    @method_decorator(logout_required)
    def get(self, request):
        """
        renders corporate and college form
        """
        context = {
            'signup_form' : SignUpForm()
        }
        return render(request, 'signup.html', context)

    @method_decorator(logout_required)
    def post(self, request):
        """
        Check the role and accordingly validate the post data
        """
        try:
            role = request.POST['role']
            pass1 =  request.POST['password1']
            pass2 =  request.POST['password2']
            if pass1 != pass2:
                print(f"password dont match {pass1}, {pass2}")
                return redirect(reverse_lazy('signup'))

            if role == ShortRoleType.NGO or role == ShortRoleType.VOLUNTEER:
                print(request.FILES)
                form = SignUpForm(request.POST, request.FILES)  # need to pass request.FILES as well to handle file uploads
                if form.is_valid():
                    print("Form is valid")
                    email = form.cleaned_data.get('email')
                    username = form.cleaned_data.get('username')
                    password= form.cleaned_data.get('password1')
                    logo = form.cleaned_data.get('logo')
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    address = form.cleaned_data.get('address')
                    phone = form.cleaned_data.get('phone')
                    website = form.cleaned_data.get('website')
                    socials = form.cleaned_data.get('socials')
                    bio = form.cleaned_data.get('bio')
                    causes = form.cleaned_data.get('causes')
                    no_of_employees = form.cleaned_data.get('no_of_employees')
                    # achievements = form.cleaned_data.get('achievements')
                    causes = form.cleaned_data.get('causes')


                    print(f"hello here {logo}")
                    if logo:
                        logo_name = logo.name
                    else:
                        logo_name = None

                    if role == ShortRoleType.NGO:
                        user = NGOModel.objects.create(username=username, email=email, 
                        password=password, role=ShortRoleType.NGO, profile_image=logo_name
                        ,interests=causes,phone=phone,company_name=first_name,address=address,
                        website=website,bio=bio)
                    else:
                        print("in")
                        user = VolunteerModel.objects.create(username=username, email=email, 
                        password=password, role=ShortRoleType.VOLUNTEER, profile_image=logo_name
                        ,interests=causes,phone=phone, first_name=first_name , last_name=last_name,bio=bio)
                    
                    user.set_password(password)
                    user.save()

                    # handle logo file upload
                    if logo:
                        with open(f"media/{logo_name}", "wb+") as f:
                            for chunk in logo.chunks():
                                f.write(chunk)
                    print("user created")
                    return redirect(reverse_lazy('home'))

                else:
                    print("Form data is invalid")
            else:
                print("invalid role")
            return redirect(reverse_lazy('signup'))
        except Exception as e:
            print(f"some error occurred {e}")
            return redirect(reverse_lazy('home'))



def dashboard(request):
    if(request.user.is_authenticated):
        event_of_volunteer = []
        events_of_ngo = events.objects.filter(ngo_id=request.user.id)
        currentEvents = 0
        no_of_hours = 0
        volunteer_events = volunteer_event.objects.all()

        if request.user.role != "VOLUNTEER":
            ok(request)

            ngo = NGOModel.objects.get(id=request.user.id) 
            AllEvents = events.objects.all()
            for e in AllEvents:
                if e.ngo_id == ngo:
                    currentEvents +=1
            print(events_of_ngo)
            for e in events_of_ngo:
                for i in all_user_events:
                    for j in all_user_events[i]:
                        if e.e_id == j:
                            volunteers_of_events[e.e_name] = []
            for e in events_of_ngo:
                print("in")
                for i in all_user_events:
                    print(i)
                    for j in all_user_events[i]:
                        print(j)
                        if e.e_id == j:
                            volunteers_of_events[e.e_name] += [i]

            

        else:       
            volunteer = VolunteerModel.objects.get(id=request.user.id)
            # volunteer_events_A = volunteer_event.objects.filter(v_id=volunteer)

            for v in volunteer_events:
                if v.v_id == volunteer:
                    event_of_volunteer.append(v.e_id)
                    no_of_hours +=  v.hours 
                    currentEvents +=1
           


        
        # for event in events_of_ngo:
        #     num_volunteers = event.volunteer_event_set.filter(v_id__ngo_id=ngo).count()
        #     print(f"Event Name: {event.e_name}, Num Volunteers: {num_volunteers}")
        # volunteer_event_list = {}
        # for v in volunteer_events:
        #     volunteer_event_list[v.e_id.e_id] = []

        # for v in volunteer_events:
        #     volunteer_event_list[v.e_id.e_id] += [str(v.v_id.id)]
        # print(volunteer_event_list)
        # print(events_of_ngo)
        # no_of_volunteers = 0
        # checked_volunteers = []
        # for e in events_of_ngo:
        #     if e.e_id in volunteer_event_list.keys():
        #         # and e.e_id not in checked_volunteers
        #         for vol in volunteer_event_list[e.e_id]:
        #             print(e.e_id)
        #             print(volunteer_event_list[1])
        #             print(vol)
        #             # for v in vol:
        #             #     if v not in checked_volunteers:
        #             #         no_of_volunteers += 1
        #             #         hecked_volunteers.append([vol])
        # print(no_of_volunteers)
        # print(request.user.ngomodel.event_set.all())

        print(volunteers_of_events)
        return render(request,'dashboard.html',context={"events_list": events_of_ngo,
                                                        "no_of_events": currentEvents,
                                                        "no_of_hours":no_of_hours,
                                                        'event_of_volunteer': event_of_volunteer,
                                                        'volunteers_of_events': volunteers_of_events})
    else:
        return redirect(reverse_lazy('login'))


def profile(request):
       return dashboard(request)

def logout_view(request):
    logout(request)
    return redirect('/')



