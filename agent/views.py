from django.shortcuts import render, redirect
from django.http import HttpResponse
from adminss.models import Roles
from adminss.forms import RolesForm
from .forms import AgentRegistrationForm
from django.contrib.auth import authenticate

# Create your views here.

def AgentRegistration(request):
    if request.method == 'POST':
        r_form = AgentRegistrationForm(data=request.POST)
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
            return redirect('home')
    else:
        r_form = AgentRegistrationForm()
        c_form = RolesForm()
    return render(request, 'agent/agentregistration.html', {'r_form':r_form, 'c_form':c_form})