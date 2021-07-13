from django.db.models.fields import BooleanField
from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, Record
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, HabitRecordForm

# Create your views here.
def homepage(request):
    return render(request, "habittracker/homepage.html")

@login_required
def profile_page(request):
    return render(request, "habittracker/profile_page.html")

@login_required
def list_habit(request):
    habit = Habit.objects.all()
    return render(request, "habittracker/list_habit.html", {"habit": habit})


@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.created_date = timezone.now()
            habit.save()
            return redirect('list_habit')
    else:
        form = HabitForm()
    return render(request, 'habittracker/add_habit.html', {'form': form})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.created_date = timezone.now()
            habit.save()
            return redirect('list_habit')
    else:
        form = HabitForm()
    return render(request, 'habittracker/add_habit.html', {'form': form})


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect('list_habit')
    return render(request, 'habittracker/delete_habit.html', {'habit': habit})

@login_required
def display_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        return redirect('list_habit')
    return render(request, 'habittracker/display_habit.html', {'habit': habit})


def add_record(request,pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST": 
        form = HabitRecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit=habit
            record.save()
            return redirect('display_habit', pk=habit.pk)
        else:
            form = HabitRecordForm()
        return render(request, 'habittracker/add_record.html', {'form': form, 'habit': habit})
