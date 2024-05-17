from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from App.forms import LoginForm, customerForm, ManagerForm




# Create your views here.
def base1(request):
    return render(request,'home.html')




def regManager(request):
    form1=LoginForm()
    form2=ManagerForm()
    if request.method=='POST':
            form1=LoginForm(request.POST)
            form2=ManagerForm(request.POST,request.FILES)
            if form1.is_valid() and form2.is_valid():
                a=form1.save(commit=False)
                a.is_worksmanager=True
                a.save()
                user1=form2.save(commit=False)
                user1.user=a
                user1.save()
                return redirect('dashboard')

    return render(request,'Manager_base/signup.html',{'form1':form1,'form2':form2})

def regCustomer(request):
    form3=LoginForm()
    form4=customerForm()
    if request.method=='POST':
            form3=LoginForm(request.POST)
            form4=customerForm(request.POST)

            if form3.is_valid() and form4.is_valid():
                a=form3.save(commit=False)
                a.is_customer=True
                a.save()
                user1=form4.save(commit=False)
                user1.user=a
                user1.save()
                return redirect('login_view')

    return render(request,'Customer_base/signup.html',{'form3':form3,'form4':form4})

def login_view(request):
    if request.method == 'POST':
     username = request.POST.get('user')
     password = request.POST.get('password')
     user = authenticate(request, username=username, password=password)
     if user is not None:
        login(request, user)
        if user.is_staff:
            return redirect('adminPage')
        elif user.is_worksmanager:
            return redirect('managerPage')
        elif user.is_customer:
            return redirect('base2')
    else:
        messages.info(request, "invalid credentials")
    return render(request, 'login_page/signin.html')
