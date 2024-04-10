from django.db import models

# Create your models here.
class RewardHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    current_balance = models.FloatField()
    sid = models.CharField(max_length=255)  # идентификатор сессии
    uid = models.CharField(max_length=255)  # идентификатор пользователя
    amount = models.FloatField()  # сумма баланса
    currency_name = models.CharField(max_length=255)  # название валюты
    currency_id = models.CharField(max_length=255)  # идентификатор валюты
