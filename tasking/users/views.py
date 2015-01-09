from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import (
	AuthenticationForm, UserRegisterForm, PasswordChangeForm, PasswordResetForm
)
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import (
	FormView, CreateView, UpdateView, DeleteView, DetailView, ListView
)

from tasks.models import Task

from .models import User
from .forms import UserRegisterForm, UserUpdateForm


class ListUser(ListView):
	model = User
	template_name = 'list_user.html'


class DetailUser(DetailView):
	model = User
	template_name = 'detail_user.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailUser, self).get_context_data(*args, **kwargs)
		context['task_set'] = Task.objects.filter(user_task=self.get_object().id)
		return context


class CreateUser(CreateView):
	model = User
	template_name = 'manage_user.html'
	form_class = UserRegisterForm

	def get_context_data(self, *args, **kwargs):
		context = super(CreateUser, self).get_context_data(*args, **kwargs)
		context['action'] = reverse('create-user')
		return context

	def get_success_url(self):
		return reverse('list-user')


class UpdateUser(UpdateView):
	model = User
	template_name = 'manage_user.html'
	form_class = UserUpdateForm

	def get_object(self):
		return User.objects.get(pk=self.request.user.id)

	def get_context_data(self, *args, **kwargs):
		context = super(UpdateUser, self).get_context_data(*args, **kwargs)
		context['action'] = reverse('update-user')
		context['update'] = True
		return context


class DeleteUser(DeleteView):
	model = User
	template_name = 'manage_user.html'


class LoginUser(FormView):
	form_class = AuthenticationForm
	template_name = 'user_login.html'

	def form_valid(self, form):
		login(self.request, form.get_user())
		if self.request.session.test_cookie_worked():
			self.request.session.delete_test_cookie()
		return HttpResponseRedirect('/tasks')

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))


class ChangePasswordUser(FormView):
	form_class = PasswordChangeForm
	template_name = 'change_password.html'

	def get_object(self):
		return User.objects.get(pk=self.request.user.id)


def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
