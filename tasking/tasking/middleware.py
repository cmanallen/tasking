from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect

class LoginRequiredMiddleware(object):
  def __init__(self):
    self.require_login_path = getattr(settings, 'REQUIRE_LOGIN_PATH', '/users/login')

  def process_request(self, request):
    if request.path != self.require_login_path and request.user.is_anonymous():
      if request.POST:
        return login(request)
      else:
        return HttpResponseRedirect('%s' % (self.require_login_path))
