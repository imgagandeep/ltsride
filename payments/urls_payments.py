from django.urls import path
from payments import views

urlpatterns = [
    path("payments", views.payments, name="payments"),
    path("ride-payment/<id>", views.paymentMode, name="ride-payment"),
    path("payment/thanks", views.handlerequest, name="payment/thanks"),
]
