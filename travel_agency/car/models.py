from django.db import models

# Create your models here.

class Car(models.Model):
	name = models.CharField(max_length=250)
	number = models.CharField(max_length=30)
	capacity = models.IntegerField()
	fair = models.FloatField()

