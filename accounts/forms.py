from django import forms
from django.contrib.auth.forms import UserCreationForm
from multiselectfield.forms.fields import MultiSelectFormField
from .models import CAUSE_CHOICES
from .choices import ShortRoleType

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    first_name = forms.CharField()
    last_name = forms.CharField()
    # logo = forms.ImageField(required=False)
    address = forms.CharField()
    phone = forms.IntegerField()
    website = forms.URLField()
    socials = forms.CharField()
    bio = forms.CharField(required=False, widget=forms.Textarea)
    causes = MultiSelectFormField(choices=CAUSE_CHOICES)
    no_of_employees = forms.IntegerField()
    achievements = forms.IntegerField()
    role = forms.ChoiceField(choices= ShortRoleType.choices)