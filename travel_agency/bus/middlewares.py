from django.shortcuts import render
class ErrorHandler: # ErrorHandler(login_view)
	def __init__(self, view):
		self.view=view 

	def __call__(self, request, *args, **kwargs):
		print("executing before view processing")
		resp = self.view(request, *args, **kwargs)
		print("executing after view processing")
		if resp.status_code==404:
			return render(request, "bus/404.html")
		return resp

