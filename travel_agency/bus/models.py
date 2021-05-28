from django.db import models
 

# Create your models here.  

class Bus(models.Model): 
	passinger_name =models.CharField(max_length = 250) 
	bus_number =models.CharField(max_length = 50) 
	pickup_point =models.CharField(max_length = 250) 
	droping_point =models.CharField(max_length = 250) 
	price =models.FloatField() 

class Car(models.Model):
	name = models.CharField(max_length=250)
	number = models.CharField(max_length=30)
	capacity = models.IntegerField()
	fair = models.FloatField()
	


class Passenger(models.Model):
	name = models.CharField(max_length = 250)
	phone = models.CharField(max_length = 11)
	dob = models.DateField()
	address = models.TextField(blank=True,default="")
	is_driver = models.BooleanField(default = False)

	def __str__(self):
		return self.name 
 
class Trip(models.Model):
	statuses = [("draft","draft"),("inprogress","inprogress"),("done","done")]
	
	source = models.CharField(max_length = 250)
	destination = models.CharField(max_length = 250)
	no_of_kms = models.IntegerField()
	status = models.CharField(max_length = 250,choices=statuses)		 
	driver = models.ForeignKey(Passenger,on_delete=models.PROTECT)
	Passengers = models.ManyToManyField(Passenger,related_name = 'trip_passengers')

	def get_passengers(self):
		return[i.name for i in self.Passengers.all()]

	def get_passengers_str(self):
		return ",".join(self.get_passengers())
	