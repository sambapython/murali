from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def car_home(request):
	#return HttpResponse("car home")
	# render will create a httpresponse object with the code of home.html file.
	return render(request, "home.html")

