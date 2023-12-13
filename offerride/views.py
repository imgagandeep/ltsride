from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.conf import settings
import datetime
import re

from offerride.models import travel_ride

# Create your views here.


# Basic view for routing
def offer_ride(request):
    if request.method == "POST":
        source = request.POST["source"]
        destination = request.POST["destination"]
        seats = request.POST["seats"]
        date = request.POST["date"]
        time = request.POST["time"]
        distance = request.POST["distance"]

        distance_miles = 0
        price = 0
        actual_distance = re.findall("\d+", distance)

        for i in actual_distance:
            distance_miles = i
            break

        miles = 1.609344
        distance_km = float(float(distance_miles) * miles)
        price = int(2 * distance_km)

        travel_distance = int(distance_km)

        context = {
            "source": source,
            "destination": destination,
            "seats": seats,
            "date": date,
            "time": time,
            "price": price,
            "travel_distance": travel_distance,
        }
        return render(request, "offer-ride-complete.html", context)
    else:
        context = {"google_api_key": settings.GOOGLE_API_KEY}
        return render(request, "offer-ride.html", context)


# Basic view for displaying a map
def offer_ride_complete(request):
    if request.method == "POST":
        source = request.POST["source"]
        destination = request.POST["destination"]
        seats = request.POST["seats"]
        date = request.POST["date"]
        time = request.POST["time"]
        price = request.POST["price"]
        distance = request.POST["distance"]
        timestamp = datetime.datetime.now()

        user_info = request.POST.get("user")
        user = User.objects.get(username=User.objects.get(first_name=user_info))
        ride_detail = travel_ride.objects.create(
            source=source,
            destination=destination,
            seats=seats,
            travel_date=date,
            travel_time=time,
            price=price,
            distance=distance,
            timestamp=timestamp,
            user=user,
        )
        ride_detail.save()
        return redirect("/your-rides")
    else:
        return render(request, "offer-ride-complete.html")
