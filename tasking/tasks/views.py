from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from tasks.models import Task, Comment, Attachment
from tasks.forms import TaskForm, TaskCommentForm

# Tasks
class ListTask(ListView):
	model = Task
	template_name = 'list_task.html'

class DetailTask(DetailView):
	model = Task
	template_name = 'detail_task.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailTask, self).get_context_data(*args, **kwargs)
		context['comments'] = Comment.objects.filter(task=self.get_object().id)
		context['attachments'] = Attachment.objects.filter(task=self.get_object().id)
		context['comment_form'] = TaskCommentForm
		return context

class CreateTask(CreateView):
	model = Task
	template_name = 'manage_task.html'
	form_class = TaskForm

	def get_context_data(self, **kwargs):
		context = super(CreateTask, self).get_context_data(**kwargs)
		context['action'] = reverse('create-task')
		return context

class UpdateTask(UpdateView):
	model = Task
	template_name = 'manage_task.html'
	form_class = TaskForm

	def get_context_data(self, **kwargs):
		context = super(UpdateTask, self).get_context_data(**kwargs)
		context['action'] = reverse('update-task', kwargs={
			'pk': self.get_object().id,
		})
		return context

	def get_success_url(self):
		return reverse('list-task')

class DeleteTask(DeleteView):
	model = Task
	template_name = 'manage_task.html'

	def get_success_url(self):
		return reverse('list-task')

def create_comment(request):
	if request.method == 'POST':
		request.POST['user'] = request.user.id
		form = TaskCommentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/tasks/%s' % request.POST['task'])
		else:
			return HttpResponseRedirect('/')
