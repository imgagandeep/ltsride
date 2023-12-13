from django.urls import path
from register import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/login/", views.login, name="accounts/login"),
    path("register", views.sign_up, name="register"),
    path("register/otp", views.otp, name="register/otp"),
    path("change-password", views.change_password, name="change-password"),
    path("logout", views.logout, name="logout"),
    # Password Reset
    path(
        "password-reset", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset-done",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
