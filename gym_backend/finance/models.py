from django.db import models
from members.models import Member

# Create your models here.

class Wallet(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
