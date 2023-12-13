from django.shortcuts import redirect, render
from django.contrib import messages
import datetime

from home.models import contact

# Create your views here.


# Home
def home(request):
    return render(request, "home.html")


# About Us
def about(request):
    return render(request, "about-us.html")


# Contact Us
def contact_us(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        email_address = request.POST["email_address"]
        mobile_number = request.POST["mobile_number"]
        query = request.POST["query"]
        timestamp = datetime.datetime.now()

        user = contact(
            full_name=full_name,
            email_address=email_address,
            mobile_number=mobile_number,
            query=query,
            timestamp=timestamp,
        )
        user.save()
        messages.info(request, "Thanks for sending a query!!!")
        return redirect("contact")
    else:
        return render(request, "contact.html")
