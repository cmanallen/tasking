from django.conf.urls import patterns, include, url
import users.views

urlpatterns = patterns('',
  # Users
  url(r'^login$', users.views.LoginUser.as_view(),
      name='login-user'),
  url(r'^logout$', users.views.user_logout,
      name='logout-user'),
  url(r'^create$', users.views.CreateUser.as_view(),
      name='create-user'),
  url(r'^$', users.views.ListUser.as_view(),
      name='list-user'),
  url(r'^profile/(?P<pk>\d+)/$', users.views.DetailUser.as_view(),
      name='detail-user'),
  url(r'^update/(?P<pk>\d+)/$', users.views.UpdateUser.as_view(),
      name='update-user'),
  url(r'^change_password/$', 'django.contrib.auth.views.password_change',
      name='change-password'),
)
