from django.shortcuts import render
from .models import Team

# Create your views here.


def team(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'teams/team.html', context)
