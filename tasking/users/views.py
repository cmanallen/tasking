from django.shortcuts import render, RequestContext, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse

# User Management
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

# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# User Register View
def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponse('User created succcessfully.')
        else:
            form = UserRegisterForm()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('register.html', context)
    else:
        return HttpResponseRedirect('/')