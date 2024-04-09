from django.db import models

# Create your models here.
class RewardHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    current_balance = models.IntegerField()
    added_balance = models.IntegerField()
