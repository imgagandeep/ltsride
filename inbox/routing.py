from django.urls import re_path as url
from inbox import consumers

websocket_urlpatterns = [
    url(r"^ws$", consumers.ChatConsumer.as_asgi()),
]
