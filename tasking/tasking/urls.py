from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import tasks.views
import projects.views
import users.views
import teams.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # Tasks
    url(r'^tasks/$', tasks.views.ListTask.as_view(),
    	name='list-task'),
    url(r'^tasks/(?P<pk>\d+)/$', tasks.views.DetailTask.as_view(),
    	name='detail-task'),
    url(r'^tasks/create$', tasks.views.CreateTask.as_view(),
    	name='create-task'),
    url(r'^tasks/update/(?P<pk>\d+)/$', tasks.views.UpdateTask.as_view(),
    	name='update-task'),
    url(r'^tasks/delete/(?P<pk>\d+)/$', tasks.views.DeleteTask.as_view(),
    	name='delete-task'),
    # Projects
    url(r'^projects/$', projects.views.ListProject.as_view(),
        name='list-project'),
    url(r'^projects/(?P<pk>\d+)/$', projects.views.DetailProject.as_view(),
        name='detail-project'),
    url(r'^projects/create$', projects.views.CreateProject.as_view(),
        name='create-project'),
    url(r'^projects/update/(?P<pk>\d+)/$', projects.views.UpdateProject.as_view(),
        name='update-project'),
    url(r'^projects/delete/(?P<pk>\d+)/$', projects.views.DeleteProject.as_view(),
        name='delete-project'),
    # Users
    url(r'^user/login$', users.views.user_login,
        name='login-user'),
    url(r'^user/logout$', users.views.user_logout,
        name='logout-user'),
    # Teams
)
