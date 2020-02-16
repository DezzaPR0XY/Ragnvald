from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.


def index(request):
  return render(request,"login_reg/login.html")

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')
      confirm_pw = form.cleaned_data.get('confirm_pw')

      user = authenticate(name_first=first_name, name_last=last_name, password=password, email=email)
      login(request, user)
      return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'login_reg/login.html', {'form': form})

def login(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      print(form.fields())
  else:
    form = UserCreationForm()
  return render(request, "login_reg/login.html", {'form': form})
