from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.

# index -> '/signin$'
def index(request):
	print """
	Testing from views$#!!!"""
	# User.objects.all().delete()
	return render(request, "login/index.html")

# register -> '/register$'
def register(request):
	print "testing register route!!!"	
	results = User.objects.validate(request.POST)   # Returned results from validation. 
	if results['status'] == True:
		user = User.objects.creator(request.POST)
		# print user.password 
		messages.success(request, "User successfully createdd!!!")
	else:
		for error in results['errors']:
			messages.error(request, error)
	return redirect("/signin")

# Login -> '/login$'
def login(request):
    results = User.objects.loginValidator(request.POST)
    if results['status'] == False:
        messages.error(request, 'Your email or password is incorrect, try again!!')
        return redirect('/')
    # otherwise login in the user and put him in session
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name
    request.session['id'] = results['user'].id     
    # print request.session['first_name']  
    # print request.session["id"]
    # print request.session["email"] 
    # return redirect('/home')
    return redirect('/') # This is home

# def home(request):
# 	return render(request, "login/homepage.html")