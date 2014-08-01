from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from teams.models import Team

# Create your views here.
class ListTeam(ListView):
	model = Team
	template_name = 'list_team.html'

class DetailTeam(DetailView):
	model = Team
	template_name = 'detail_team.html'

class CreateTeam(CreateView):
	model = Team
	template_name = 'manage_team.html'

class UpdateTeam(UpdateView):
	model = Team
	template_name = 'manage_team.html'

class DeleteTeam(DeleteView):
	model = Team
	template_name = 'manage_team.html'