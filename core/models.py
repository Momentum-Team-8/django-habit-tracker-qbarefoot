from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
class Habit(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    goal = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class HabitTracker(models.Model):

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    results = models.PositiveIntegerField()
    date = models.DateField(null=True)