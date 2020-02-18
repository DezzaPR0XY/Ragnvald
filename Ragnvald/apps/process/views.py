from django.shortcuts import render, HttpResponse
from .models import *

def index(request):

  return HttpResponse("this is the equivalent of @app.route('/')!")