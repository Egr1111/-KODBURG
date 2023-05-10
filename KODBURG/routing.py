from django.urls import path
from . import consumer

websocket_urlpatterns = [
    path("ws/ac/<str:room_name>/", consumer.MyWebConsumer.as_asgi()),

]
