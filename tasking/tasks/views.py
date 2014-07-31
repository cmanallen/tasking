from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from tasks.models import Task, Comment
from tasks.forms import TaskForm

# Tasks
class ListTask(ListView):
	model = Task
	template_name = 'list_task.html'

class DetailTask(DetailView):
	model = Task
	template_name = 'detail_task.html'

class CreateTask(CreateView):
	model = Task
	template_name = 'manage_task.html'
	form_class = TaskForm

	def get_context_data(self, **kwargs):
		context = super(CreateTask, self).get_context_data(**kwargs)
		context['action'] = reverse('create-task')
		return context

	def get_success_url(self):
		return reverse('list-task')

class UpdateTask(UpdateView):
	model = Task
	template_name = 'manage_task.html'
	form_class = TaskForm

	def get_context_data(self, **kwargs):
		context = super(UpdateTask, self).get_context_data(**kwargs)
		context['action'] = reverse('update-task', kwargs={'pk': self.get_object().id})
		return context

	def get_success_url(self):
		return reverse('list-task')

class DeleteTask(DeleteView):
	model = Task
	template_name = 'manage_task.html'

	def get_success_url(self):
		return reverse('list-task')

# Comments
class CreateComment(CreateView):
	model = Comment
	template_name = 'detail_task.html'

	def get_context_data(self, **kwargs):
		context = super(CreateComment, self).get_context_data(**kwargs)
		context['action'] = reverse('create-comment')
		return context

	def get_success_url(self, **kwargs):
		return reverse('detail-task', kwargs={'pk': self.get_object().id})