from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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


# Many-to-many Views
def create_user_team(request):
	if request.method == 'POST':
		team_id = request.POST['id']
		team = Team.objects.filter(id=team_id)
		for t in team:
			t.user_team.add(request.user.id)
	return HttpResponseRedirect(reverse('detail-team', kwargs={'pk':team_id}))

def remove_user_team(request):
	if request.method == 'POST':
		team_id = request.POST['id']
		team = Team.objects.filter(id=team_id)
		for t in team:
			t.user_team.remove(request.user.id)
	return HttpResponseRedirect(reverse('detail-team', kwargs={'pk':team_id}))
