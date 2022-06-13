from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("chat/", views.chat, name="chat"),
    path("chat/<str:room_name>/", views.room, name="chat-room"),
]
