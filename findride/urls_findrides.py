from django.urls import path
from findride import views

urlpatterns = [
    path("find-ride", views.find_ride, name="find-ride"),
    path("find-ride-complete", views.find_ride_complete, name="find-ride-complete"),
    path("save-ride/<id>", views.saveride, name="save-ride"),
]
