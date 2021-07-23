from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . models import Bus
from . models import Car
from . models import Passenger
from . models import Trip
from bus.forms import VehicleForm
from bus.utilities import loginCheckDecorator
# Create your views here.

#############################Bus Information#############
 
# def primary(request):
# 	return render(request,'bus/primary.html')


# def home(request):
# 	data = Bus.objects.all()
# 	return render(request,'bus/home.html',{'data':data})


#CREATE PROCESS
def bus_create(request):
	message = ""
	if request.method == 'POST':
		data = request.POST
		bus_object = Bus(passinger_name=data.get('bus_Passinger_Name'), 
			bus_number=data.get('bus_Bus_Number'),
			pickup_point=data.get('bus_Pickup_Point'), 
			droping_point=data.get('bus_Droping_Point'),
			price=data.get('bus_Price'))
		bus_object.save()
		message = "Bus Detailes Saved in DataBase!!"
		return redirect("/bus/")
		
	return render(request,'bus/create.html',{'msg':message})



#UPDATAE PROCESS
def bus_update(request,pk):
	bus_obj = Bus.objects.get(id=pk)
	if request.method == "POST":
		data = request.POST
		bus_obj.passinger_name = data.get('passinger_name')
		bus_obj.bus_number = data.get('bus_number')
		bus_obj.pickup_point = data.get('pickup_point')
		bus_obj.droping_point = data.get('droping_point')
		bus_obj.price = data.get('price')
		bus_obj.save()
		return redirect("/bus/")

	return render(request,'bus/update.html',{'bus':bus_obj})




# DELETE PROCESS is Direct Process

# def bus_delete(request,pk):
# 	bus_obj = Bus.objects.get(id = pk)
# 	bus_obj.delete()
# 	return redirect("/bus/")



#DELETE PROCESS is Optional Process
def bus_delete(request,pk):
	bus_obj = Bus.objects.get(id = pk)
	if request.method == "POST":
		if "YES" in request.POST:
			bus_obj.delete()
		return redirect("/bus/")

	else:
		return render(request,'bus/delete.html',{'bus':bus_obj})



###########################Car Information###############

def home1(request):
	car_data = Car.objects.all()
	return render(request,'bus/home1.html',{'data':car_data})

#Create Process
def car_create(request):
	message = ""
	if request.method == 'POST':
		form = VehicleForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("/car/car1/")
		else:
			message = form.errors
	else:
		form = VehicleForm() 
	return render(request,'bus/create1.html',{'msg':message,"form":form})


#UPDATAE PROCESS
def car_update(request,pk):
	car_obj = Car.objects.get(id=pk)
	if request.method == "POST":
		data = request.POST
		car_obj.name = data.get('name')
		car_obj.number = data.get('number')
		car_obj.capacity = data.get('capacity')
		car_obj.fair = data.get('fair')
		car_obj.save()
		return redirect("/car/car1/")

	return render(request,'bus/update1.html',{'car':car_obj})


#DELETE PROCESS is Optional Process
def car_delete(request,pk):
	car_obj = Car.objects.get(id = pk)
	if request.method == "POST":
		if "YES" in request.POST:
			car_obj.delete()
		return redirect("/car/car1/")

	else:
		return render(request,'bus/delete1.html',{'car':car_obj})

#############################Passenger information###########
#@login_required(login_url="/login/")
# added login_url in settings
@login_required
def home2(request):
	passenger_data = Passenger.objects.all()
	return render(request,'bus/home2.html',{'data':passenger_data})


#Create Process
@login_required
def passenger_create(request):
	message = ""
	if request.method == 'POST':
		data = request.POST
		passenger_object =Passenger (name=data.get("pass_name"),
			phone=data.get("pass_phone"),
			dob=data.get("pass_dob"),
			address=data.get("pass_address"),
			is_driver=data.get("pass_driver"),
			created_by=request.user
			)

		passenger_object.save()
		message = 'Passenger created successfully'
		return redirect("/passenger/passenger1/")
		
	return render(request,'bus/create2.html',{'msg':message})
	

#UPDATAE PROCESS
def passenger_update(request,pk):
	passenger_obj = Passenger.objects.get(id=pk)
	if request.method == "POST":
		data = request.POST
		passenger_obj.name = data.get('name')
		passenger_obj.phone = data.get('phone')
		passenger_obj.dob = data.get('dob')
		passenger_obj.address = data.get('address')
		passenger_obj.is_driver = data.get('is_driver')
		passenger_obj.save()
		return redirect("/passenger/passenger1/")

	return render(request,'bus/update2.html',{'passenger':passenger_obj})


#DELETE PROCESS is Optional Process
def passenger_delete(request,pk):
	passenger_obj = Passenger.objects.get(id = pk)
	if request.method == "POST":
		if "YES" in request.POST:
			passenger_obj.delete()
		return redirect("/passenger/passenger1/")

	else:
		return render(request,'bus/delete2.html',{'passenger':passenger_obj})

####################Trip information##############

def home3(request):
	trip_data = Trip.objects.all()
	return render(request,'bus/home3.html',{'data':trip_data})


#Create Process
def trip_create(request): 
	message = ""
	statuses = [i[0] for i in Trip.statuses]
	drivers = Passenger.objects.filter(is_driver=True)  #ForeignKey process
	passengers = Passenger.objects.all()
	context = {"passengers":passengers,"drivers":drivers,
	"statuses":statuses}
	if request.method == 'POST':
		data = request.POST
		driver_objs = Passenger.objects.filter(is_driver=True,id=data.get("trip_driver"))
		trip_object =Trip(source=data.get("trip_source"),
			destination=data.get("trip_destination"),
			no_of_kms=data.get("trip_kms"),
			status=data.get("trip_status"),
			driver=driver_objs[0])
		trip_object.save() 
		for passenger_id in data.getlist("trip_passenger"):
			passenger_obj =Passenger.objects.get(id= passenger_id)   #ManyToMany Process
			trip_object.Passengers.add(passenger_obj)
		 

		message = 'Passenger created successfully'
		return redirect("/trip/trip1/")
	context.update({"msg":message})
	return render(request,'bus/create3.html',context)
	

#UPDATAE PROCESS
def trip_update(request,pk):
	drivers = Passenger.objects.filter(is_driver=True)  
	passengers = Passenger.objects.all()
	context = {"passengers":passengers,"drivers":drivers}

	trip_obj = Trip.objects.get(id=pk)
	if request.method == "POST":
		data = request.POST
		trip_obj.source = data.get('source')
		trip_obj.destination = data.get('destination')
		trip_obj.no_of_kms = data.get('no_of_kms')
		trip_obj.status = data.get('status')
		trip_obj.driver = data.get('driver')

		#trip_obj.driver = data.get('Passengers')

		for passenger_id in data.getlist('Passengers'):
			passenger_obj =Passenger.objects.get(id= passenger_id)   #ManyToMany Process
			trip_obj.Passengers.add(passenger_obj)
		trip_obj.save()

	
		return redirect("/trip/trip1/")
	 
	return render(request,'bus/update3.html',{'trip':trip_obj})




#DELETE PROCESS is Optional Process
def trip_delete(request,pk):
	trip_obj = Trip.objects.get(id = pk)
	if request.method == "POST":
		if "YES" in request.POST:
			trip_obj.delete()
		return redirect("/passenger/passenger1/")

	else:
		return render(request,'bus/delete3.html',{'trip':trip_obj})
