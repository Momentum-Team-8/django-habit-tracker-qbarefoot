from django.db.models.fields import BooleanField
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Habit, Record
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, HabitRecordForm
from django.http import JsonResponse

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

def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.created_date = timezone.now()
            habit.save()
            return redirect('add_habit')
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
    habit.delete()
    return redirect('list_habit')