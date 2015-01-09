from django.conf.urls import patterns, include, url
import tasks.views

urlpatterns = patterns('',
  # Tasks
  url(r'^$', tasks.views.ListTask.as_view(),
    name='list-task'),
  url(r'^(?P<pk>\d+)/$', tasks.views.DetailTask.as_view(),
    name='detail-task'),
  url(r'^create$', tasks.views.CreateTask.as_view(),
    name='create-task'),
  url(r'^update/(?P<pk>\d+)/$', tasks.views.UpdateTask.as_view(),
    name='update-task'),
  url(r'^delete/(?P<pk>\d+)/$', tasks.views.DeleteTask.as_view(),
    name='delete-task'),
  # Tasks Comments
  url(r'^comments/create', tasks.views.create_comment,
    name='create-task-comment'),
  # Tasks Attachments
  url(r'^attachments/create', tasks.views.create_attachment,
    name='create-task-attachment'),
  # Tasks Complete
  url(r'^complete', tasks.views.complete_task,
    name='complete-task'),
  # Tasks UserTask
  url(r'^work', tasks.views.create_usertask,
    name='create-task-user'),
)
