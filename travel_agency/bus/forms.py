from django import forms
from bus.models import Car
#forms.Form
#forms.ModelForm

class VehicleForm(forms.ModelForm):
	class Meta:
		model = Car
		fields = "__all__"
		#fields = ['name','number']
		#exclude=['fair']

		


class SampleForm(forms.Form):
	name = forms.CharField(label="Vehicle name", max_length=250)
	number = forms.IntegerField(label="Vehicle number")

