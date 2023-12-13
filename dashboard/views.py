from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from dashboard.models import travel_prefrence, add_car

# Create your views here.


# Dashboard
def dashbaord(request):
    if not request.user.is_authenticated:
        return redirect("accounts/login/")
    else:
        current_user = request.user
        try:
            travel_pref_detail = travel_prefrence.objects.get(user=current_user.pk)
        except travel_prefrence.DoesNotExist:
            travel_pref_detail = None
        try:
            car_details = add_car.objects.get(user=current_user.pk)
        except add_car.DoesNotExist:
            car_details = None
        return render(
            request,
            "dashboard.html",
            {
                "current_user": current_user,
                "travel_pref_detail": travel_pref_detail,
                "car_details": car_details,
            },
        )


# Travel Preferences
def travel_pref(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        chattiness = request.POST["chattiness"]
        music = request.POST["music"]
        smoking = request.POST["smoking"]
        pets = request.POST["pets"]
        user_info = request.POST.get("user")
        user = User.objects.get(username=User.objects.get(first_name=user_info))

        if travel_prefrence.objects.filter(user=user).exists():
            travel_detail = travel_prefrence.objects.get(user=user.pk)
            travel_detail.chattiness = chattiness
            travel_detail.music = music
            travel_detail.smoking = smoking
            travel_detail.pets = pets
            travel_detail.user = user
        else:
            travel_detail = travel_prefrence.objects.create(
                chattiness=chattiness,
                music=music,
                smoking=smoking,
                pets=pets,
                user=user,
            )

        travel_detail.save()
        return redirect("dashboard")
    else:
        user_detail = User.objects.get(pk=pk)
        try:
            travel_pref_detail = travel_prefrence.objects.get(user=user_detail.pk)
        except travel_prefrence.DoesNotExist:
            travel_pref_detail = None

        context = {"user_detail": user_detail, "travel_pref_detail": travel_pref_detail}
        return render(request, "travel-pref.html", context)


# Add Car Details
def add_car_detail(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        country = request.POST["country"]
        plate_number = request.POST["plate_number"]
        brand = request.POST["brand"]
        model = request.POST["model"]
        car_image = request.FILES["car_image"]
        user_info = request.POST.get("user")
        user = User.objects.get(username=User.objects.get(first_name=user_info))

        if add_car.objects.filter(user=user).exists():
            car_detail = add_car.objects.get(user=user.pk)
            car_detail.country = country
            car_detail.plate_number = plate_number
            car_detail.brand = brand
            car_detail.model = model
            car_detail.car_image = car_image
            car_detail.user = user
        else:
            car_detail = add_car.objects.create(
                country=country,
                licence_plate_number=plate_number,
                brand=brand,
                model=model,
                car_image=car_image,
                user=user,
            )

        car_detail.save()
        return redirect("dashboard")
    else:
        user_detail = User.objects.get(pk=pk)
        try:
            car_details = add_car.objects.get(user=user_detail.pk)
        except add_car.DoesNotExist:
            car_details = None

        context = {"user_detail": user_detail, "car_details": car_details}
        return render(request, "add-car.html", context)
