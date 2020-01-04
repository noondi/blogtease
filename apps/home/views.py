from django.shortcuts import render, HttpResponse, redirect
from ..login.models import User
# from .models import Trip
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, "home/homepage.html")

def jarbas1(request):
	return render(request, "home/jarbas1.html")

def bsides2018vancouver(request):
	return render(request, "home/bsides2018vancouver.html")

def born2root(request):
	return render(request, "home/born2root.html")

def billymadison(request):
	return render(request, "home/billymadison.html")

def spjerome1(request):
	return render(request, "home/spjerome1.html")

def logout(request):    
    # request.session.flush()
    request.session.clear()
    return redirect('/')
