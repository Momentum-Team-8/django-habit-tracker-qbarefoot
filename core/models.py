from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint

from datetime import date

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    target = models.PositiveIntegerField()
    created_date = models.DateField(default=date.today)

    def __repr__(self):
        return f"<Habit name={self.name}>"

    def __str__(self):
        return self.name

class Record(models.Model):
    habit = models.ForeignKey(Habit, null=True, on_delete=models.CASCADE, related_name="records")
    outcome = models.PositiveIntegerField()
    date = models.DateField(default=date.today)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'outcome', 'date'], name='unique_record')
        ]