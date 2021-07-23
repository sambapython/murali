from django import forms
from bus.models import Car
from django.contrib.auth.models import User
#forms.Form
#forms.ModelForm

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username',"password"]
		 


class VehicleForm(forms.ModelForm):
	# first_name=fields.CharField(label="Vehicle First name", max_length=250)
	# last_name=fields.CharField(label="Vehicle last name", max_length=250)
	class Meta:
		model = Car
		fields = "__all__"
		#fields = ['name','number']
		#exclude=['fair']

	
		

		


class SampleForm(forms.Form):
	name = forms.CharField(label="Vehicle name", max_length=250)
	number = forms.IntegerField(label="Vehicle number")

