from django import forms
from .models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'user',
            'name',
            'target',
            'created_date',
            ]


class HabitRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'habit',
            'outcome',
            'date',
            ]