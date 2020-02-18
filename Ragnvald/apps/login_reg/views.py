# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import CsrfViewMiddleware
# from .forms import SignUpForm
from .models import User
# Create your views here.


def index(request):
  if request.method == 'POST':
    print(request.POST)
    form = request.POST
    if form['route'] == 'register':
      errors = User.objects.is_valid(form)
      if len(errors) > 0:
        print(errors)
        return render(request, 'login_reg/login.html', errors)
      user = User.objects.create(name_first=form['first_name'], name_last=form['last_name'], email=form['email'], password=form['password'])
      print(user)
      print("Success!")
      return redirect('/taskboard')
    if form['route'] == 'login':
      user = User.objects.filter(email=form['email'])
      print(user)
      if len(user) > 0:
        if user.password == form['password']:
          print("Success!")
          return redirect('/taskboard')
  return render(request, 'login_reg/login.html')


def register(request):
#   if request.method == 'POST':
#     form = SignUpForm(request.POST)
#     print(form.is_valid())
#     if form.is_valid():
#       form.save()
#       first_name = form.cleaned_data.get('first_name')
#       print(first_name)
#       last_name = form.cleaned_data.get('last_name')
#       print(last_name)
#       email = form.cleaned_data.get('email')
#       print(email)
#       password = form.cleaned_data.get('password')
#       print(password)
#       confirm_pw = form.cleaned_data.get('confirm_pw')
#       print("first_name:%s \nlast_name:%s \nemail:%s \npassword:%s \nconfirm_pw:%s" %(first_name,last_name,email,password,confirm_pw))

#       user = authenticate(name_first=first_name, name_last=last_name, password=password, email=email)
#       print(user)
#       login(request, user)
#       return redirect('/')
#       return redirect('home')
#   else:
#     form = SignUpForm()
  # return redirect('/')
#   return render(request, 'login_reg/login.html', {'form': form})
  return render(request, 'login_reg/login.html')

def login(request):
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       print(form.fields())
#   else:
#     form = UserCreationForm()
  # return render(request, "login_reg/login.html", {'form': form})
  return render(request, "login_reg/login.html")
