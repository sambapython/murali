from car.views import car_home


from django.urls import path

urlpatterns = [
   path("",car_home)
]