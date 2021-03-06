from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,  PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from adminss.models import Roles
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _



#Agent Registration Form
class AgentRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}