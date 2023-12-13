from django.urls import path
from dashboard import views

urlpatterns = [
    path("dashboard", views.dashbaord, name="dashboard"),
    path(
        "dashboard/travel-pref/<int:pk>",
        views.travel_pref,
        name="dashboard/travel-pref",
    ),
    path("dashboard/add-car/<int:pk>", views.add_car_detail, name="dashboard/add-car"),
]
