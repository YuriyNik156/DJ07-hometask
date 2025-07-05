from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.username} ({self.telegram_id})"