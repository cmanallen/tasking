from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('django_messages.urls')),
<<<<<<< HEAD
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
      # Tasks Comments
      url(r'^tasks/comments/create', tasks.views.create_comment,
        name='create-task-comment'),
      # Tasks Attachments
      url(r'^tasks/attachments/create', tasks.views.create_attachment,
        name='create-task-attachment'),
      # Tasks Complete
      url(r'^tasks/complete', tasks.views.complete_task,
        name='complete-task'),
      # Tasks UserTask
      url(r'^tasks/work', tasks.views.create_usertask,
        name='create-task-user'),
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
    url(r'^users/login$', users.views.LoginUser.as_view(),
        name='login-user'),
    url(r'^users/logout$', users.views.user_logout,
        name='logout-user'),
    url(r'^users/create$', users.views.CreateUser.as_view(),
        name='create-user'),
    url(r'^users/$', users.views.ListUser.as_view(),
        name='list-user'),
    url(r'^users/profile/(?P<pk>\d+)/$', users.views.DetailUser.as_view(),
        name='detail-user'),
    url(r'^users/update/$', users.views.UpdateUser.as_view(),
        name='update-user'),
    url(r'^users/change_password/$', users.views.ChangePasswordUser.as_view(),
        name='change-password'),
    # Teams
    url(r'^teams/$', teams.views.ListTeam.as_view(),
        name='list-team'),
    url(r'^teams/(?P<pk>\d+)/$', teams.views.DetailTeam.as_view(),
        name='detail-team'),
    url(r'^teams/create$', teams.views.CreateTeam.as_view(),
        name='create-team'),
    url(r'^teams/update/(?P<pk>\d+)/$', teams.views.UpdateTeam.as_view(),
        name='update-team'),
    url(r'^teams/delete/(?P<pk>\d+)/$', teams.views.DeleteTeam.as_view(),
        name='delete-team'),
=======
    url(r'^users/', include('users.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^teams/', include('teams.urls')),
>>>>>>> c6656b17ba60ef73a0f37768c68dc2abfdd01366
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
