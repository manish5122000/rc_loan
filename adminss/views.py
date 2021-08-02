from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Roles
from .forms import RolesForm, AdminRegistrationForm
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    return render(request, 'adminss/home.html')

#Registration
def RegistrationPage(request):
    return render(request, 'adminss/registerpage.html')


def AdminRegistration(request):
    if request.method == 'POST':
        r_form = AdminRegistrationForm(data=request.POST)
        c_form = RolesForm(data=request.POST)
        if r_form.is_valid() and c_form.is_valid():
            user = r_form.save() 
            user.save()
            cate = c_form.save(commit=False)
            cate.user = user
            cate.save()
            username = r_form.cleaned_data.get('username')
            raw_password = r_form.cleaned_data.get('password')
            category = c_form.cleaned_data.get('category')
            user = authenticate(username=username, password=raw_password, role=category)
            return redirect('login')
    else:
        r_form = AdminRegistrationForm()
        c_form = RolesForm()
    return render(request, 'adminss/adminregistration.html', {'r_form':r_form, 'c_form':c_form})


        




