from django.views.generic import CreateView, TemplateView
from django.utils.decorators import method_decorator
from .models import NGOModel, VolunteerModel
from .forms import SignUpForm
from .custom_decorators import logout_required
import logging
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .choices import RoleType, ShortRoleType
from django.contrib.auth import get_user_model
User = get_user_model()

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

            print(role)
            if role == ShortRoleType.NGO or role == ShortRoleType.VOLUNTEER:
                form = SignUpForm(request.POST)
                # check email entered is already is in database
                # redirect_url = check_email(request, request.POST.get('email',None))
                # if redirect_url != None:
                #     return redirect(redirect_url)
                if form.is_valid():
                    print("Form is valid")
                    email = form.cleaned_data.get('email')
                    username = form.cleaned_data.get('username')
                    password= form.cleaned_data.get('password1')
                    
                    if role == ShortRoleType.NGO:
                        user = NGOModel.objects.create(username=username, email=email, 
                        password=password, role=ShortRoleType.NGO)
                    else:
                        user = VolunteerModel.objects.create(username=username, email=email, 
                        password=password, role=ShortRoleType.VOLUNTEER)
                    
                    user.set_password(password)
                    user.save()
                else:
                    print("Form data is invalid")
            else:
                print("invalid role")
            return redirect(reverse_lazy('signup'))
        except Exception as e :
            print(f"some error occured {e}")
            return redirect(reverse_lazy('home'))