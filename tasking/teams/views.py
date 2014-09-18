from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from teams.models import Team
from users.models import User

# Create your views here.
class ListTeam(ListView):
	model = Team
	template_name = 'list_team.html'

class DetailTeam(DetailView):
	model = Team
	template_name = 'detail_team.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailTeam, self).get_context_data(*args, **kwargs)
		context['members'] = User.objects.filter(
			team=self.get_object().id
		)
		return context

class CreateTeam(CreateView):
	model = Team
	template_name = 'manage_team.html'

class UpdateTeam(UpdateView):
	model = Team
	template_name = 'manage_team.html'

class DeleteTeam(DeleteView):
	model = Team
	template_name = 'manage_team.html'
