from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from findride.models import save_ride
from ltsride import settings
from payments import checksum
from payments.models import transaction
import random

# Create your views here.


# Payments
def payments(request):
    user = request.user.username
    user = User.objects.get(username=user)
    payment_detail = transaction.objects.filter(transaction_by=user)

    context = {"payment_detail": payment_detail}
    return render(request, "payments.html", context)


# Paytm Payment Mode
MERCHANT_KEY = settings.MERCHANT_KEY


def paymentMode(request, id):
    order = save_ride.objects.get(id=id)
    user = request.user.username
    client_id = User.objects.get(username=user)
    amount = order.price
    order_id = random.randint(1000, 10000)

    param_dict = {
        "MID": settings.MERCHANT_ID,
        "ORDER_ID": str(order_id),
        "CUST_ID": str(client_id.id),
        "TXN_AMOUNT": str(amount),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        "CALLBACK_URL": "http://127.0.0.1:8000/payment/thanks",
    }

    param_dict["CHECKSUMHASH"] = checksum.generateSignature(param_dict, MERCHANT_KEY)

    return render(request, "paytm.html", {"params": param_dict})


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == "CHECKSUMHASH":
            checksum_response = form[i]

    verify = checksum.verifySignature(response_dict, MERCHANT_KEY, checksum_response)

    if verify:
        if response_dict["RESPCODE"] == "01":
            print("Payment Successful!!")
            id = response_dict.get("ORDERID")
            order = save_ride.objects.get(id=1)
            user = order.user
            client_id = User.objects.get(username=user)
            save_transaction = transaction.objects.create(
                transaction_to=order.travel_mate,
                customer_id=client_id.id,
                source=order.source,
                destination=order.destination,
                amount=order.price,
                order_id=order.id,
                transaction_by=user,
            )
            save_transaction.save()
        else:
            print("Payment was not successful because. " + response_dict["RESPMSG"])

    return render(request, "thanks.html", {"response": response_dict})
