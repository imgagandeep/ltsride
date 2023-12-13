from django.urls import path
from userprofile import views

urlpatterns = [
    path("my-profile", views.user_profile, name="my-profile"),
    path("my-profile/bio/<int:pk>", views.bio, name="my-profile/bio"),
    path("my-profile/govt-id", views.govtId, name="govt-id"),
    path(
        "my-profile/govt-id/passport/<int:pk>",
        views.passport,
        name="my-profile/govt-id/passport",
    ),
    path(
        "my-profile/govt-id/aadhar-card/<int:pk>",
        views.aadharCard,
        name="my-profile/govt-id/aadhar-card",
    ),
    path(
        "my-profile/personal-detail/<int:pk>",
        views.personal_detail,
        name="my-profile/personal-detail",
    ),
    path("delete-account/<int:pk>", views.delete_account, name="delete-account"),
]
