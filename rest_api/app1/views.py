from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Category
import json

# Create your views here.

class CategoryAPIView(APIView):

	def delete(self, request, cat_id):
		data = {"message":"Success"}
		status_code = 200
		try:
			cat = Category.objects.get(id=cat_id)
			cat.delete()
		except Exception as err: 
			data['message'] = str(err)
			status_code=404
		return Response(data, status=status_code)

	def put(self, request, cat_id):
		data = {"message":"Success"}
		status_code = 200
		try:
			cat = Category.objects.get(id=cat_id)
			request_data = request.data
			cat.name = request_data.get("name")
			cat.save()
		except Exception as err: 
			data['message'] = str(err)
			status_code=404
		return Response(data, status=status_code)


	def get(self, request,cat_id=None):
		items = []
		cats = []
		status_code=200
		data = {"message":"Success","items":items}
		if cat_id:
			try:
				cats = Category.objects.get(id=cat_id)
				if cats:
					cats = [cats]
			except Exception as err:
				data['message'] = str(err)
				status_code=404
		else:
			cats = Category.objects.all() 
		for cat in cats:
			items.append({"name":cat.name})
		return Response(data,status=status_code)

	def post(self, request):
		data = request.data
		cat = Category(name=data.get("name"))
		try:
			cat.save()
			raise Exception("Category not created.")
			message="Category %s inserted successfully!" % cat.name
			status_code = 201
		except Exception as err:
			message = str(err)
			status_code=400
		return  Response({"message":message}, status=status_code)