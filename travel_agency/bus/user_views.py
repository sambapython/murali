from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.modelsimport DoesNotExist
from bus.forms import UserForm
def register(request):
	errors=""
	if request.method=="POST":
		form = UserForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			return redirect("/")
		else:
			errors=form.errors
	else:
		form = UserForm()
	return render(request, "bus/register.html",
		{"form":form,"errors":errors})

def logout_view(request):
	logout(request)
	return redirect("/")

def login_view(request):
	errors = ""
	if request.method == "POST":
		data = request.POST
		username=data.get("username")
		password=data.get("password")
		#try:
			#user = User.objects.get(username=username, password=password)
			#return redirect("/")
		#except User.DoesNotExist as err:
		#	errors="username password invalid"	
		user = authenticate(username=username, password=password)
		#request.session['attribute'] = "value"
		login(request=request,user=user) # it will set request.user and request.session
		if user:
			return redirect("/")
		else:
			errors="username password invalid"	
	return render(request,"bus/login.html",{"errors":errors})