from django.db import models
from members.models import Coach

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()

    def __str__(self):
        return f"{self.course.title} - {self.date}"
