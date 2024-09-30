from django.urls import path
from oscarbot.views import bot_view
from .apps import SellerBotConfig


app_name = SellerBotConfig.name

urlpatterns = [
    path('bot<str:token>/', bot_view),
]
