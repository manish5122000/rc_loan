from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, UsernameField,  PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Roles
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _

#Admin Registration Form
class AdminRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}


class Admin_form(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


#Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password', 'class':'form-control'}))


#Change Password Form
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=('Old Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))

    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())

    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))


# Reset Password Form
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email'),max_length=255, widget=forms.EmailInput
        (attrs={'autocomplete':'email','class':'form-control'}))



#Confirm Reset Password Form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())
    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))

#Roles Selction
class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['category']
        widget = {'category':forms.TextInput(attrs={'class':'form-control'})

        }