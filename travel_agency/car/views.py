from django.shortcuts import render, redirect
from django.http import HttpResponse
from car.models import Car

# Create your views here.
def car_delete(request, pk):
	car_obj = Car.objects.get(id=pk)
	car_obj.delete()
	return  redirect("/car/")

def car_update(request, pk):
	car_obj = Car.objects.get(id=pk)
	if request.method == "POST":
		data = request.POST 
		car_obj.name=data.get("name")
		car_obj.fair=data.get("fair")
		car_obj.number = data.get("number")
		car_obj.capacity = data.get("capacity")
		car_obj.save()
		return redirect("/car/")

	return render(request, "car/update.html",{"car":car_obj})

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
		return redirect("/car/")
	return render(request, "car/create.html",{"msg":message})

def car_home(request):
	#return HttpResponse("car home")
	# render will create a httpresponse object with the code of home.html file.
	data = Car.objects.all()
	return render(request, "car/home.html",{"data":data})

