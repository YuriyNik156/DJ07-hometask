from rest_framework import serializers
from .models import TelegramUser

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        models = TelegramUser
        fields = ["telegram_id", "username"]