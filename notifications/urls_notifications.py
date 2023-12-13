from django.urls import path
from notifications import views

urlpatterns = [
    path("notifications", views.show_notifications, name="notifications"),
]
