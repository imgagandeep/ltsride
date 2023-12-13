from django.shortcuts import redirect, render
from django.contrib.auth.models import auth, User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER

# from django.http import request
from django.template.loader import render_to_string

# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.views.generic.base import View
# import os
import random
import datetime

from register.models import register, verify_otp

# Create your views here.


# Register
def sign_up(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["first_name"]
        gender = request.POST["gender"]
        date_of_birth = request.POST["date_of_birth"]
        email = request.POST["email"]
        mobile_number = request.POST["mobile_number"]
        aadhar_number = request.POST["aadhar_number"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!!!")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!!!")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                ext_user = register(
                    gender=gender,
                    date_of_birth=date_of_birth,
                    mobile_number=mobile_number,
                    user=user,
                    aadhar_number=aadhar_number,
                )
                user.is_active = False
                user.save()
                ext_user.save()

                # Send OTP
                timestamp = datetime.datetime.now()
                current_site = get_current_site(request)
                email_otp = random.randint(100000, 999999)
                verify_otp.objects.create(
                    email_otp=email_otp, timestamp=timestamp, user=user
                )
                subject = "Verify Email"
                message = render_to_string(
                    "verify-email.html",
                    {
                        "user": first_name,
                        "domain": current_site.domain,
                        "verification_code": email_otp,
                    },
                )

                send_mail(
                    subject,
                    message,
                    EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return render(request, "otp.html", {"user": user})
        else:
            messages.info(request, "Confirm Password is not matched!!!")
            return redirect("register")
    else:
        return render(request, "register.html")


# Email OTP
def otp(request):
    if request.method == "POST":
        get_email_otp = request.POST["emailotp"]
        if get_email_otp:
            user_info = request.POST.get("user")
            user = User.objects.get(username=user_info)
            if (
                int(get_email_otp)
                == verify_otp.objects.filter(user=user).last().email_otp
            ):
                user.is_active = True
                user.save()
                messages.info(request, "Email Verified")
                return redirect("/accounts/login/")
            else:
                messages.info(request, "You entered a Wrong OTP")
                return render(request, "otp.html", {"user": user})
        else:
            return render(request, "otp.html")
    else:
        return render(request, "otp.html")


# Login
def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]

        try:
            user = auth.authenticate(
                username=User.objects.get(email=username), password=password
            )
        except:
            user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        elif not User.objects.filter(email=username).exists():
            messages.info(request, "Invalid Credentails!!!")
            return redirect("/accounts/login/")
        elif not User.objects.get(email=username).is_active:
            # Fetch User detail from database
            user = User.objects.get(username=User.objects.get(email=username))

            # Send OTP
            timestamp = datetime.datetime.now()
            current_site = get_current_site(request)
            email_otp = random.randint(100000, 999999)
            verify_otp.objects.create(
                email_otp=email_otp, timestamp=timestamp, user=user
            )
            subject = "Verify Email"
            message = render_to_string(
                "verify-email.html",
                {
                    "user": user.first_name,
                    "domain": current_site.domain,
                    "verification_code": email_otp,
                },
            )
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            messages.info(request, "Please verify your account!!!")
            return render(request, "otp.html", {"user": user})
        else:
            messages.info(request, "Invalid Credentails!!!")
            return redirect("/accounts/login/")
    else:
        return render(request, "login.html")


# Change Password
def change_password(request):
    if request.method == "POST":
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]

        user = User.objects.get(id=request.user.id)
        check = user.check_password(old_password)

        if check == True:
            user.set_password(new_password)
            user.save()
            user = auth.authenticate(username=user.username, password=new_password)
            if user is not None:
                auth.login(request, user)
                return redirect("/dashboard")
        else:
            messages.info(request, "Incorrect Current Password!!!")
            return redirect("change-password")
    else:
        return render(request, "change-password.html")


# Logout
def logout(request):
    auth.logout(request)
    return redirect("/")
