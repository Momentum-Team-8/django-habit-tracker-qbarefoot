from django.contrib import admin
from.models import HabitTracker, User, Habit, HabitTracker


# Register your models here.
admin.site.register(User)
admin.site.register(Habit)
admin.site.register(HabitTracker)
