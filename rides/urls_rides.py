from django.urls import path
from rides import views

urlpatterns = [
    path("your-rides", views.your_rides, name="your-rides"),
    path("delete-ride/<id>", views.delete_ride, name="delete-ride"),
    path("delete-find-ride/<id>", views.delete_find_ride, name="delete-find-ride"),
]
