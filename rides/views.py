from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import datetime

from dashboard.models import travel_prefrence
from findride.models import save_ride
from offerride.models import travel_ride
from payments.models import transaction
from userprofile.models import story

# Create your views here.


# Rides
def your_rides(request):
    user = User.objects.get(id=request.user.id)
    ride_detail = travel_ride.objects.filter(user=user)
    rides = save_ride.objects.all().filter(user=user)
    payment_status = transaction.objects.all()
    today = datetime.now()
    today_date = datetime.date(today)
    today_time = datetime.time(today)

    orders = []
    for i in payment_status:
        orders.append(i.order_id)

    queryset = 0
    if not ride_detail.exists():
        if not rides.exists():
            queryset = None

    prefDetail = []
    for data in rides:
        mate = data.travel_mate
        username = User.objects.get(username=mate)

        try:
            pref_detail = travel_prefrence.objects.get(user=username)
        except travel_prefrence.DoesNotExist:
            pref_detail = None
        prefDetail.append(pref_detail)

    bioDetail = []
    for data in rides:
        mate = data.travel_mate
        username = User.objects.get(username=mate)

        try:
            ext_bio = story.objects.get(user=username)
        except story.DoesNotExist:
            ext_bio = None
        bioDetail.append(ext_bio)

    try:
        travel_pref_detail = travel_prefrence.objects.get(user=user)
    except travel_prefrence.DoesNotExist:
        travel_pref_detail = None
    try:
        bio_detail = story.objects.get(user=user)
    except story.DoesNotExist:
        bio_detail = None

    context = {
        "ride_detail": ride_detail,
        "rides": rides,
        "travel_pref_detail": travel_pref_detail,
        "bio_detail": bio_detail,
        "prefDetail": prefDetail,
        "bioDetail": bioDetail,
        "queryset": queryset,
        "today_date": today_date,
        "orders": orders,
    }
    return render(request, "your-rides.html", context)


# Delete Offer Ride
def delete_ride(request, id):
    ride = travel_ride.objects.get(id=id)
    if request.method == "POST":
        ride.delete()
        return redirect("/your-rides")
    else:
        return render(request, "delete-ride.html")


# Delete Find Ride
def delete_find_ride(request, id):
    ride = save_ride.objects.get(id=id)
    if request.method == "POST":
        ride.delete()
        return redirect("/your-rides")
    else:
        return render(request, "delete-ride.html")
