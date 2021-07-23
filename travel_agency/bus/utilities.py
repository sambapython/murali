from django.shortcuts import redirect
def loginCheckDecorator(fun):
	def inner(request,*args, **kwargs):
		if request.user.is_authenticated:
			return fun(*args, **kwargs)
		return redirect("/login")
	return inner
