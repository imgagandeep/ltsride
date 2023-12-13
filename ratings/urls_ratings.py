from django.urls import path, include
from ratings import views

urlpatterns = [
    path("ratings/<str:name>", views.ratings, name="ratings"),
    path("reviews/<str:name>", views.reviews, name="reviews"),
]
