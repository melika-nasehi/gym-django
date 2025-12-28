from members.models import Member
from django.db import models
from members.models import Member

# Create your models here.


class Wallet(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name="wallet")
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"Wallet({self.member}) - {self.balance}"


class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CARD = "CARD", "Card"
        CASH = "CASH", "Cash"
        ONLINE = "ONLINE", "Online"

    class PaymentStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SUCCESS = "SUCCESS", "Success"
        FAILED = "FAILED", "Failed"

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="payments")
    amount = models.IntegerField()
    method = models.CharField(max_length=10, choices=PaymentMethod.choices, default=PaymentMethod.ONLINE)
    status = models.CharField(max_length=10, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.amount} - {self.status}"
