from django.db import models
from members.models import Member
from classes.models import Session
from django.db import models
from members.models import Member
from classes.models import Session

# Create your models here.

class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="bookings")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="bookings")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["member", "session"],
                name="unique_member_session_booking",
            )
        ]

    def __str__(self):
        return f"{self.member} - {self.session}"


class Attendance(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="attendance")
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"Attendance for {self.booking}"
