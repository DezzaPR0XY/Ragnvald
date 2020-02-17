from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import CsrfViewMiddleware
from apps.login_reg.forms import SignUpForm
# Create your views here.


def index(request):
  # return render(request,"login_reg/login.html")
# def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            confirm_pw = form.cleaned_data.get('password1')
            user = authenticate(first_name=first_name, last_name=last_name, password=password, confirm_pw=confirm_pw)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'login_reg/login.html', {'form': form})


def register(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    print(form)
    print(form.is_valid())
    if form.is_valid():
      form.save()
      first_name = form.cleaned_data.get('first_name')
      print(first_name)
      last_name = form.cleaned_data.get('last_name')
      print(last_name)
      email = form.cleaned_data.get('email')
      print(email)
      password = form.cleaned_data.get('password')
      print(password)
      confirm_pw = form.cleaned_data.get('confirm_pw')
      print("first_name:%s \nlast_name:%s \nemail:%s \npassword:%s \nconfirm_pw:%s" %(first_name,last_name,email,password,confirm_pw))

      user = authenticate(name_first=first_name, name_last=last_name, password=password, email=email)
      print(user)
      login(request, user)
      return redirect('/')
      return redirect('home')
  else:
    form = SignUpForm()
  return redirect('/')
  return render(request, 'login_reg/login.html', {'form': form})

def login(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      print(form.fields())
  else:
    form = UserCreationForm()
  return render(request, "login_reg/login.html", {'form': form})
