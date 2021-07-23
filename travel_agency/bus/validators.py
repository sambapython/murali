from django.core.exceptions import ValidationError
def name_validate(name):
	name1=name.replace(" ","")
	if name1.isalnum():
		return name
	#raise Exception("name invalid")
	raise ValidationError("name invalid")