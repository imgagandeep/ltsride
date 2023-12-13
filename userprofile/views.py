from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from django.contrib import messages
# from django.http import request
import datetime

from userprofile.models import story, govt_id
from register.models import register

# Create your views here.


# Profile Detail
def user_profile(request):
    current_user = request.user
    other_detail = register.objects.get(user=current_user.pk)
    return render(
        request,
        "my-profile.html",
        {"current_user": current_user, "other_detail": other_detail},
    )


# Bio
def bio(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        bio = request.POST["bio"]
        timestamp = datetime.datetime.now()
        user_info = request.POST.get("user")
        user = User.objects.get(username=User.objects.get(first_name=user_info))

        if story.objects.filter(user=user).exists():
            user_story = story.objects.get(user=user.pk)
            user_story.story = bio
            user_story.timestmap = timestamp
            user_story.user = user
        else:
            user_story = story.objects.create(story=bio, timestamp=timestamp, user=user)

        user_story.save()
        return redirect("my-profile")
    else:
        user_detail = User.objects.get(pk=pk)
        try:
            story_details = story.objects.get(user=user_detail.pk)
        except story.DoesNotExist:
            story_details = None
        return render(
            request,
            "bio.html",
            {"user_detail": user_detail, "story_details": story_details},
        )


# Verify govt. ID
def govtId(request):
    current_user = request.user
    context = {"current_user": current_user}
    return render(request, "govt-id.html", context)


# Passport
def passport(request, pk):
    if request.method == "POST":
        passport_image = request.FILES["passport_image"]
        user_info = request.POST.get("user")
        user = User.objects.get(username=User.objects.get(first_name=user_info))

        if govt_id.objects.filter(user=user).exists():
            save_passport = govt_id.objects.get(user=user.pk)
            save_passport.passport = passport_image
            save_passport.user = user
        else:
            save_passport = govt_id.objects.create(passport=passport_image, user=user)

        save_passport.save()
        return redirect("/my-profile/govt-id")
    else:
        current_user = request.user
        context = {"current_user": current_user}
        return render(request, "passport.html", context)


# Aadhar Card
def aadharCard(request, pk):
    if request.method == "POST":
        aadhar_image = request.FILES["aadhar_image"]
        user_info = request.POST.get("user")
        user = User.objects.get(username=User.objects.get(first_name=user_info))

        if govt_id.objects.filter(user=user).exists():
            save_aadhar = govt_id.objects.get(user=user.pk)
            save_aadhar.aadhar_card = aadhar_image
            save_aadhar.user = user
        else:
            save_aadhar = govt_id.objects.create(aadhar_card=aadhar_image, user=user)

        save_aadhar.save()
        return redirect("/my-profile/govt-id")
    else:
        current_user = request.user
        context = {"current_user": current_user}
        return render(request, "aadhar-card.html", context)


# Personal Detail
def personal_detail(request, pk):
    user = User.objects.get(pk=pk)
    ext_user = register.objects.get(user=user.pk)
    if request.method == "POST":
        # print(request.FILES['user_image'])
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["first_name"]
        user_image = request.FILES.get("user_image", "")

        # user = User.objects.get(pk = pk).update(first_name = first_name, last_name = last_name, username = username)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username

        if user_image != "":
            ext_user.user_image = user_image
        ext_user.user = user

        user.save()
        ext_user.save()

        # user_detail = User.objects.get(pk = pk)
        # other_detail = register.objects.get(user = user.pk)
        return render(
            request,
            "personal-detail.html",
            {"user_detail": user, "other_detail": ext_user},
        )
    else:
        user_detail = User.objects.get(pk=pk)
        other_detail = register.objects.get(user=user_detail.pk)
        return render(
            request,
            "personal-detail.html",
            {"user_detail": user_detail, "other_detail": other_detail},
        )


# Delete Account
@login_required
def delete_account(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("/register")
    else:
        return render(request, "delete-account.html")
