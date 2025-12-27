from django.db import models
from members.models import Member
from classes.models import Session

# Create your models here.


class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    is_present = models.BooleanField()