from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .models import userinfo
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def sign_view(request):
    if request.method ==  'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else: 
      initial_data = { 'username':'','password1':'','password2':""}
      form = UserCreationForm(initial=initial_data)
    return render(request,'authpage/signup.html',{'form':form})

def login_view(request):
    if request.method ==  'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
      initial_data = { 'username':'','password':''}
      form = AuthenticationForm(initial=initial_data)
    return render(request,'authpage/login.html',{'form':form})

def index_view(request):
    return render(request,'authpage/index.html')
@login_required
def success_view(request):
    return render(request,'authpage/success.html')

#@login_required
def info(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    job = request.POST.get('job')
    address = request.POST.get('address')
    phone = request.POST.get('phone')

    new_userinfo = userinfo(name=name, age=age, job=job, email=email, address=address, phone=phone)
    new_userinfo.save()
    
    return render(request, 'authpage/info.html')

def logout_view(request):
    logout(request)
    return redirect('login')