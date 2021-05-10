from car.views import car_home, car_create, car_update, car_delete


from django.urls import path

urlpatterns = [
   path("",car_home),
   path("create/", car_create),
   path("update/<int:pk>/", car_update), #car_update(request, pk=4)
   path("delete/<int:pk>/", car_delete),

]