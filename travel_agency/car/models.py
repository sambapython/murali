from django.db import models

# Create your models here.

class Car(models.Model):
	name = models.CharField(max_length=250)
	number = models.CharField(max_length=30)
	capacity = models.IntegerField()
	fair = models.FloatField()

class Passenger(models.Model):
	name = models.CharField(max_length=250)
	phone = models.CharField(max_length=11)
	dob = models.DateField()
	address = models.TextField(blank=True, default="")
	is_driver = models.BooleanField(default=False)



class Trip(models.Model):
	source = models.CharField(max_length=250)
	destination = models.CharField(max_length=250)
	no_of_kms = models.IntegerField()
	status = models.CharField(choices=[("draft","draft"),("inporgress","inprogress"),("done","done")])
	driver = models.ForeignKey(Passenger, on_delete=models.PROTECT)
	passengers = models.ManyToManyField(Passenger)
