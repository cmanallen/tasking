from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Count

from utils.models import TimeStamp


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class TeamManager(models.Manager):
	
	def get_query_set(self):
		return super(TeamManager, self).get_query_set().annotate(users=Count('user_team'))


class Team(TimeStamp):
	
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()

	# Relations
	user_team = models.ManyToManyField(AUTH_USER_MODEL)

	# Manager
	objects = TeamManager()

	# Model Methods
	def get_absolute_url(self):
		return reverse('detail-team', kwargs={'pk': self.id})

	def __str__(self):
		return "%s" % self.name