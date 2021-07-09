from django.contrib import admin
from.models import Record, User, Habit, Record


# Register your models here.
admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Record)
