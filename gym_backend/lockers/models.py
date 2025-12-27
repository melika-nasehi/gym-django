from django.db import models

# Create your models here.

class Locker(models.Model):
    number = models.PositiveIntegerField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Locker {self.number}"
