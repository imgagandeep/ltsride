from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from inbox import views
from inbox.api import MessageModelViewSet, UserModelViewSet

router = DefaultRouter()
router.register(r"message", MessageModelViewSet, basename="message-api")
router.register(r"user", UserModelViewSet, basename="user-api")


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("inbox", login_required(views.inbox), name="inbox"),
]
