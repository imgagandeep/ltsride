from django.shortcuts import redirect, render
from django.conf import settings

# from django.contrib.auth.models import User
import datetime

from dashboard.models import travel_prefrence
from findride.models import save_ride
from offerride.models import travel_ride
from userprofile.models import story

# Create your views here.


# Find Ride
def find_ride(request):
    if request.method == "POST":
        source = request.POST["source"]
        destination = request.POST["destination"]
        date = request.POST["date"]

        ride_detail = travel_ride.objects.all().filter(
            source=source, destination=destination, travel_date=date
        )

        prefDetail = []
        for data in ride_detail:
            username = data.user
            try:
                pref_detail = travel_prefrence.objects.get(user=username)
            except travel_prefrence.DoesNotExist:
                pref_detail = None
            prefDetail.append(pref_detail)
        # for pref in prefDetail:
        #     print(pref.chattiness)

        bioDetail = []
        for data in ride_detail:
            username = data.user
            try:
                ext_bio = story.objects.get(user=username)
            except story.DoesNotExist:
                ext_bio = None
            bioDetail.append(ext_bio)

        context = {
            "ride_detail": ride_detail,
            "prefDetail": prefDetail,
            "bioDetail": bioDetail,
        }
        return render(request, "find-ride-complete.html", context)
    else:
        context = {"google_api_key": settings.GOOGLE_API_KEY}
        return render(request, "find-ride.html", context)


# Find Ride Complete
def find_ride_complete(request):
    return render(request, "find-ride-complete.html")


# Save Ride
def saveride(request, id):
    ride_id = travel_ride.objects.get(id=id)
    avl_seats = travel_ride.objects.get(id=id)
    if request.method == "POST":
        source = ride_id.source
        destination = ride_id.destination
        seats = ride_id.seats
        ride_seats = 1
        date = ride_id.travel_date
        time = ride_id.travel_time
        price = ride_id.price
        travel_mate = str(ride_id.user)
        timestamp = datetime.datetime.now()
        user = request.user
        available_seats = seats - 1

        save_ride_detail = save_ride.objects.create(
            source=source,
            destination=destination,
            seats=ride_seats,
            travel_date=date,
            travel_time=time,
            price=price,
            timestamp=timestamp,
            travel_mate=travel_mate,
            ride=ride_id,
            user=user,
        )

        # avl_seats = travel_ride.objects.get(id = id).update(seats = available_seats)
        avl_seats.seats = available_seats
        # avl_seats.user = travel_mate

        save_ride_detail.save()
        avl_seats.save()
        print("User Ride Saved!!!")
        return redirect("/your-rides")
    else:
        return render(request, "save-ride.html")
