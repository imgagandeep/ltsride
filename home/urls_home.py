from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us", views.about, name="about"),
    path("contact", views.contact_us, name="contact"),
]
