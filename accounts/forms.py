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
    last_name = forms.CharField(required=False)
    logo = forms.ImageField(required=False)
    address = forms.CharField(required=False)
    phone = forms.IntegerField()
    website = forms.URLField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea)
    causes = MultiSelectFormField(choices=CAUSE_CHOICES)
    no_of_employees = forms.IntegerField(required=False)
    # achievements = forms.IntegerField(required=False)
    role = forms.ChoiceField(choices= ShortRoleType.choices)

    def save(self, *args, **kwargs):
        instance = super(SignUpForm, self).save(commit=False)
        if self.cleaned_data.get('logo', None):
            logo = self.cleaned_data['logo']
            fs = FileSystemStorage()
            filename = fs.save(logo.name, logo)
            instance.logo = filename
        instance.save()
        return instance