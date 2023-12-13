from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from dashboard.models import travel_prefrence
from register.models import register
from ratings.models import user_rating
from userprofile.models import story

# Create your views here.


# Ratings
def ratings(request, name):
    username = name
    user = User.objects.get(username=username)
    rating_detail = user_rating.objects.all().filter(user=user)
    if request.method == "POST":
        rating = request.POST["rating"]
        comment = request.POST["comment"]
        submit = request.POST["user"]

        save_rating = user_rating.objects.create(
            rating=rating, comment=comment, submit_by=submit, user=user
        )
        save_rating.save()
        return redirect("/your-rides")
    else:
        image = register.objects.get(user=user)

        try:
            detail = travel_prefrence.objects.get(user=user)
        except travel_prefrence.DoesNotExist:
            detail = None
        try:
            bio = story.objects.get(user=user)
        except story.DoesNotExist:
            bio = None

        context = {
            "image": image,
            "username": username,
            "detail": detail,
            "bio": bio,
            "rating_detail": rating_detail,
        }
        return render(request, "ratings.html", context)


# Reviews
def reviews(request, name):
    username = name
    user = User.objects.get(username=username)
    rating_detail = user_rating.objects.all().filter(user=user)

    try:
        detail = travel_prefrence.objects.get(user=user)
    except travel_prefrence.DoesNotExist:
        detail = None
    try:
        bio = story.objects.get(user=user)
    except story.DoesNotExist:
        bio = None

    context = {
        "username": username,
        "detail": detail,
        "bio": bio,
        "rating_detail": rating_detail,
    }
    return render(request, "reviews.html", context)
