from django.shortcuts import render, RequestContext, render_to_response
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from users.models import User
from users.forms import UserRegisterForm

# Class Based Views
class ListUser(ListView):
    model = User
    template_name = 'list_user.html'

class DetailUser(DetailView):
    model = User
    template_name = 'detail_user.html'

class UpdateUser(UpdateView):
    model = User
    template_name = 'manage_user.html'

class DeleteUser(DeleteView):
    model = User
    template_name = 'manage_user.html'

# Create user
def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/users/login')
        else:
            form = UserRegisterForm()

        return HttpResponseRedirect('/users/create')
    else:
        return HttpResponseRedirect('/')

# Authentication
def user_login(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    return HttpResponse("Not active")
            else:
                return HttpResponse("Wrong username/password")
    return HttpResponseRedirect('/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')