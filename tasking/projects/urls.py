from django.conf.urls import patterns, include, url
import projects.views

urlpatterns = patterns('',
  # Projects
  url(r'^$', projects.views.ListProject.as_view(),
      name='list-project'),
  url(r'^(?P<pk>\d+)/$', projects.views.DetailProject.as_view(),
      name='detail-project'),
  url(r'^create$', projects.views.CreateProject.as_view(),
      name='create-project'),
  url(r'^update/(?P<pk>\d+)/$', projects.views.UpdateProject.as_view(),
      name='update-project'),
  url(r'^delete/(?P<pk>\d+)/$', projects.views.DeleteProject.as_view(),
      name='delete-project'),
)
