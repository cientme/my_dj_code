from django.shortcuts import render
from django.views import View
import random
from .forms import GameForm

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        winNum = random.randint(1, 10)
        form = GameForm()
        context = {
            'form': form,
            'wn': winNum,

            }
        return render(request, 'social/home.html', context)

    def post(self, request, *args, **kwargs):
        winNum = random.randint(1, 100)
        form = GameForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            if number == winNum:
                return render(request, 'social/win.html', {'number': number})
            if number == winNum - 2:
                return render(request, 'social/bonus.html', {'number': number})
            if number > 100 or number < 1:
                return render(request, 'social/numError.html', {'number': number})
        form = GameForm()
        context = {
            'form': form,
            'wn': winNum,
            'n': number,
            }
        return render(request, 'social/home.html', context)
