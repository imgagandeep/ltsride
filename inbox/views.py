from django.shortcuts import render

# from django.contrib.auth.models import User

# Create your views here.


# Inbox
def inbox(request):
    return render(request, "inbox.html")
