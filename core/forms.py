from django import forms
from .models import Habit, HabitTracker

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'user',
            'title',
            'goal',
            'created_date',

        ]

class HabitTrackerForm(forms.ModelForm):
    class Meta:
        model = HabitTracker
        fields = [
            'habit',
            'complete_goal',
            'date',
        ]