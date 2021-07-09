from django.db.models.fields import BooleanField
from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, Record, User
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
def list_deck(request):
    decks = Deck.objects.all()
    return render(request, "flashcards/list_deck.html", {"decks": decks})

def add_habit(request, pk):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.created_date = timezone.now()
            habit.save()
            return redirect('add_habit', pk=pk)
    else:
        form = HabitForm()
    return render(request, 'habittracker/add_habit.html', {'form': form})