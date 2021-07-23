from django.db import models
from django.contrib.auth.models import User, AbstractUser

from bus.validators import name_validate

 

# Create your models here. 

class User(AbstractUser):
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=250)



class Bus(models.Model): 
	passinger_name =models.CharField(max_length = 250,
		validators=[name_validate]) 
	bus_number =models.CharField(max_length = 50) 
	pickup_point =models.CharField(max_length = 250) 
	droping_point =models.CharField(max_length = 250) 
	price =models.FloatField() 

class Car(models.Model):
	name = models.CharField(max_length=250,
		validators=[name_validate])
	number = models.CharField(max_length=30)
	capacity = models.IntegerField()
	fair = models.FloatField()
	


class Passenger(models.Model):
	name = models.CharField(max_length = 250)
	phone = models.CharField(max_length = 11)
	dob = models.DateField()
	address = models.TextField(blank=True,default="")
	is_driver = models.BooleanField(default = False)
	created_by = models.ForeignKey(User, on_delete=models.PROTECT)

	def __str__(self):
		return self.name 
 
class Trip(models.Model):
	statuses = [("draft","draft"),("inprogress","inprogress"),("done","done"),("cancel","cancel")]
	
	source = models.CharField(max_length = 250)
	destination = models.CharField(max_length = 250)
	no_of_kms = models.IntegerField()
	status = models.CharField(max_length = 250,choices=statuses)		 
	driver = models.ForeignKey(Passenger,on_delete=models.PROTECT)
	Passengers = models.ManyToManyField(Passenger,related_name = 'trip_passengers')
	created_by = models.ForeignKey(User, on_delete=models.PROTECT)

	def get_passengers(self):
		return[i.name for i in self.Passengers.all()]

	def get_passengers_str(self):
		return ",".join(self.get_passengers())
	