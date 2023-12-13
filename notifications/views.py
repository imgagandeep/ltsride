from django.shortcuts import redirect, render

from notifications.models import notification_message
from register.models import register

# Create your views here.


# Notifications
def show_notifications(request):
    if request.method == "POST":
        news = request.POST.get("news_check")
        msgs = request.POST.get("msgs_check")
        rides = request.POST.get("rides_check")
        current_user = request.user
        user = current_user

        if notification_message.objects.filter(user=user).exists():
            notifications = notification_message.objects.get(user=user)
            notifications.news_stuff = news
            notifications.messages = msgs
            notifications.publishing_rides = rides
            notifications.user = user
        else:
            notifications = notification_message.objects.create(
                news_stuff=news, messages=msgs, publishing_rides=rides, user=user
            )

        notifications.save()
        return redirect("/my-profile")
    else:
        current_user = request.user
        other_detail = register.objects.get(user=current_user.pk)

        try:
            notifications_detail = notification_message.objects.all().filter(
                user=current_user
            )
        except notification_message.DoesNotExist:
            notifications_detail = None

        context = {
            "other_detail": other_detail,
            "notifications_detail": notifications_detail,
        }
        return render(request, "notifications.html", context)
