from django.conf.urls import patterns, include, url
import teams.views

urlpatterns = patterns('',
  # Teams
  url(r'^$', teams.views.ListTeam.as_view(),
      name='list-team'),
  url(r'^(?P<pk>\d+)/$', teams.views.DetailTeam.as_view(),
      name='detail-team'),
  url(r'^create$', teams.views.CreateTeam.as_view(),
      name='create-team'),
  url(r'^update/(?P<pk>\d+)/$', teams.views.UpdateTeam.as_view(),
      name='update-team'),
  url(r'^delete/(?P<pk>\d+)/$', teams.views.DeleteTeam.as_view(),
      name='delete-team'),
  # Join Team
  url(r'^join/$', teams.views.create_user_team,
    name='join-team'),
  # Leave Team
  url(r'^leave/$', teams.views.remove_user_team,
    name='leave-team'),
)
