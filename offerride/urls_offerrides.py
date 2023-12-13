from django.urls import path
from offerride import views

urlpatterns = [
    path("offer-ride", views.offer_ride, name="offer-ride"),
    path("offer-ride-complete", views.offer_ride_complete, name="offer-ride-complete"),
]
