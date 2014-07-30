from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from projects.models import Project

# Projects
class ListProject(ListView):
	model = Project
	queryset = Project.with_tasks.all()
	template_name = 'list_project.html'

class DetailProject(DetailView):
	model = Project
	template_name = 'detail_project.html'

class CreateProject(CreateView):
	model = Project
	template_name = 'manage_project.html'

	def get_context_data(self, **kwargs):
		context = super(CreateProject, self).get_context_data(**kwargs)
		context['action'] = reverse('create-project')
		return context

	def get_success_url(self):
		return reverse('list-project')

class UpdateProject(UpdateView):
	model = Project
	template_name = 'manage_project.html'

	def get_context_data(self, **kwargs):
		context = super(UpdateProject, self).get_context_data(*kwargs)
		context['action'] = reverse('update-project', kwargs={'pk': self.get_object().id})
		return context

	def get_success_url(self):
		return reverse('list-project')

class DeleteProject(DeleteView):
	model = Project
	template_name = 'manage_project.html'

	def get_success_url(self):
		return reverse('list-project')