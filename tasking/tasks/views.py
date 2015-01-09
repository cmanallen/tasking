from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from users.models import User

from .forms import TaskForm, TaskCommentForm, TaskAttachmentForm
from .models import Task, Comment, Attachment


class ListTask(ListView):
	model = Task
	template_name = 'list_task.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ListTask, self).get_context_data(*args, **kwargs)
		context['user_tasks'] = Task.objects.filter(user_task=self.request.user.id)[:5]
		context['tasks_due'] = Task.objects.filter(
			user_task=self.request.user.id,
		).extra(order_by=['due'])[:5]
		return context


class DetailTask(DetailView):
	model = Task
	template_name = 'detail_task.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailTask, self).get_context_data(*args, **kwargs)
		context['comments'] = Comment.objects.filter(task=self.get_object().id)
		context['attachments'] = Attachment.objects.filter(task=self.get_object().id)
		context['user_tasks'] = User.objects.filter(
			task=self.get_object().id,
		).values_list('pk', flat=True)
		context['upload_form'] = TaskAttachmentForm
		return context


class CreateTask(CreateView):
	model = Task
	template_name = 'manage_task.html'
	form_class = TaskForm

	def get_context_data(self, **kwargs):
		context = super(CreateTask, self).get_context_data(**kwargs)
		context['action'] = reverse('create-task')
		return context

	def form_valid(self, form):
		task = form.save(commit=False)
		task.created_by = self.request.user
		task.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('list-task')


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
			return HttpResponseRedirect(reverse('detail-task', kwargs={'pk': request.POST['task']}))
		else:
			return HttpResponseRedirect('/')


def create_attachment(request):
	if request.method == 'POST':
		post_values = request.POST.copy()
		post_values['user'] = request.user.id
		form = TaskAttachmentForm(post_values, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('detail-task', kwargs={'pk': request.POST['task']}))
		else:
			return HttpResponseRedirect('/')


def create_usertask(request):
	if request.method == 'POST':
		task = Task.objects.filter(id=request.POST['id'])
		if request.user.is_authenticated():
			for t in task:
				t.user_task.add(request.user.id)
		return HttpResponseRedirect(reverse('detail-task', kwargs={'pk': request.POST['id']}))


def complete_task(request):
	if request.method == 'POST':
		Task.objects.filter(id=request.POST['id']).update(status=1)
		return HttpResponseRedirect(reverse('detail-task', kwargs={'pk': request.POST['id']}))
