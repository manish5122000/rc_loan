from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,  PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import widgets
from adminss.models import Roles
from .models import Apply_Loan, Document, Personal_Information
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _



#Agent Registration Form
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}

#customer personal information
class Personal_Information_Form(forms.ModelForm):
    class Meta:
        model = Personal_Information
        fields = ['Full_Name','Mother_Name','DOB','Age','Pin_code','Work_Type','Address_Type',
        'Aadhar_Card_Number','Pan_Card_Number'
        ]
   
        widgets = { 'Full_Name':forms.TextInput(attrs={'class':'form-control'}),
                'Mother_Name':forms.TextInput(attrs={'class':'form-control'}),
                'DOB':forms.TextInput(attrs={'class':'form-control'}),
                'Age':forms.TextInput(attrs={'class':'form-control'}),
                'Pin_code':forms.TextInput(attrs={'class':'form-control'}),
                'Work_Type':forms.Select(attrs={'class':'form-control'}),
                'Address_Type':forms.Select(attrs={'class':'form-control'}),
                'Aadhar_Card_Number':forms.NumberInput(attrs={'class':'form-control'}),
                'Pan_Card_Number':forms.TextInput(attrs={'class':'form-control'}),

            }

class Document_Form(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['Front_Upload_Aadhar','Back_Upload_Aadhar', 'Upload_Pancard','Upload_Image','Upload_Income_Proof','Upload_Residence_Proof']


#loan apply
class Loan_Form(forms.ModelForm):
    class Meta:
        model = Apply_Loan
        fields = ['id','Company_Name','Salary','Amount_Need','Tenure','Rate','Loan_Status']
        widgets = {'Company_Name':forms.TextInput(attrs={'class':'form-control'}),
                'Salary':forms.TextInput(attrs={'class':'form-control'}),
                'Amount_Need':forms.TextInput(attrs={'class':'form-control'}),
                'Tenure':forms.Select(attrs={'class':'form-control'}),
                'Rate':forms.TextInput(attrs={'class':'form-control'}),
                'Loan_Status':forms.Select(attrs={'class':'form-control'}),
            }
    