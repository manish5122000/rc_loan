import re
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from adminss.models import Roles
from django.contrib.auth.models import User
from .models import Apply_Loan, Document, Personal_Information
from adminss.forms import RolesForm, Admin_form
from .forms import CustomerRegistrationForm, Document_Form, Loan_Form, Personal_Information_Form
from django.contrib.auth import authenticate

# Create your views here.

# Registration 
def CustomerRegistration(request):
    if request.method == 'POST':
        r_form = CustomerRegistrationForm(data=request.POST)
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
        r_form = CustomerRegistrationForm()
        c_form = RolesForm()
    return render(request, 'customer/customerregistration.html', {'r_form':r_form, 'c_form':c_form})

#Personal information
class Personal_Info(View):
    # code = request.GET.get(code)
    def get(self,request):
        if request.user.is_superuser == True:
            p_form = Admin_form(instance=request.user)
            users = User.objects.all()
        
        else:
            p_form = Personal_Information_Form()
            users = None
        return render(request, 'customer/personinfo.html',{'p_form':p_form, 'users':users , 'active':'btn-primary'})    
    def post(self,request):
        if request.user.is_superuser == True:
            p_form = Admin_form(request.POST, instance=request.user)
            users = User.objects.all()
        else:
            p_form = Personal_Information_Form(request.POST)
            users = None
        if p_form.is_valid():
            usr = request.user
            usr.save()
            Full_Name = p_form.cleaned_data['Full_Name']
            Mother_Name = p_form.cleaned_data['Mother_Name']
            DOB = p_form.cleaned_data['DOB']
            Age = p_form.cleaned_data['Age']
            Pin_code = p_form.cleaned_data['Pin_code']
            Work_Type = p_form.cleaned_data['Work_Type']
            Address_Type = p_form.cleaned_data['Address_Type']
            Aadhar_Card_Number = p_form.cleaned_data['Aadhar_Card_Number']
            Pan_Card_Number = p_form.cleaned_data['Pan_Card_Number']
            dash = Personal_Information(user=usr,Full_Name=Full_Name,Mother_Name=Mother_Name, DOB=DOB, Age=Age,
                            Pin_code=Pin_code, Work_Type=Work_Type, Address_Type=Address_Type,
                            Aadhar_Card_Number=Aadhar_Card_Number,Pan_Card_Number=Pan_Card_Number
            )
            dash.save()

        return render(request, 'customer/personinfo.html',{'p_form':p_form, 'users':users,'active':'btn-primary'})

#Dashboard
def dashboard(request):
    dash = Personal_Information.objects.filter(user=request.user)
    return render(request, 'customer/dashboard.html',{'dash':dash, 'active':'btn-primary'})

#Document
def Docs(request):
    if request.method == 'POST':
        d_form = Document_Form(request.POST, request.FILES, instance=request.user)
        print('ajhfaf',d_form)
        if d_form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            return redirect('dashboard')
    else:
        d_form = Document_Form(instance=request.user)
    return render(request, 'customer/document.html',{'d_form':d_form, 'active':'btn-primary'})

#apply for loan
@login_required
def loan_apply(request):
    if request.method == "POST":
        l_form = Loan_Form(request.POST)
        if l_form.is_valid():
            usr = request.user
            usr.save()
            Company_Name = l_form.cleaned_data['Company_Name']
            Salary = l_form.cleaned_data['Salary']
            Amount_Need = l_form.cleaned_data['Amount_Need']
            Tenure = l_form.cleaned_data['Tenure']
            ln = Apply_Loan(user=usr, Company_Name=Company_Name, Salary=Salary, Amount_Need=Amount_Need, Tenure=Tenure)
            ln.save()
            return redirect('dashboard')

    else:
        l_form = Loan_Form()
    return render(request, 'customer/loanapply.html',{'loan':l_form, 'active':'btn-primary'})

#Get user detail by admin
def get_user_detail(request, id):
    if request.user.is_authenticated:
        u_detail = User.objects.get(pk=id)
        p_form = Admin_form(instance=u_detail)
        return render(request, 'customer/userdetail.html', {'p_form':p_form, 'acitve':'btn-primary'})
    else:
        return redirect('login')

#
def Admin_view(request):
    adm = Apply_Loan.objects.filter(user=request.user)
    return render(request, 'customer/loanstatus.html', {'adm':adm})