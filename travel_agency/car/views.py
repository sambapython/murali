from django.shortcuts import render
from django.http import HttpResponse
from car.models import Car

# Create your views here.

def car_create(request):
	message=""
	if request.method=="POST":
		data = request.POST
		car_object = Car(name=data.get("car_name"),
			fair=data.get("car_fair"),
			capacity=data.get("car_capacity"),
			number=data.get("car_number"))
		car_object.save()
		message="car created successfully!"


	return render(request, "car/create.html",{"msg":message})

def car_home(request):
	#return HttpResponse("car home")
	# render will create a httpresponse object with the code of home.html file.
	return render(request, "car/home.html")

