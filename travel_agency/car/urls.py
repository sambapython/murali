from car.views import car_home, car_create


from django.urls import path

urlpatterns = [
   path("",car_home),
   path("create/", car_create)
]