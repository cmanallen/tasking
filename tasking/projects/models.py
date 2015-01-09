from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.db.models import Count

from utils.models import TimeStamp


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ProjectManager(models.Manager):
	def get_query_set(self):
		return super(ProjectManager, self).get_query_set().annotate(tasks=Count('task'))


class Project(TimeStamp):
	
	# Fields
	name = models.CharField(max_length=255)
	description = models.TextField()
	
	# Relations
	created_by = models.ForeignKey(AUTH_USER_MODEL)
	
	# Manager
	objects = ProjectManager()
	
	# Model Methods
	def get_absolute_url(self):
		return reverse('detail-project', kwargs={'pk': self.id})

	def __str__(self):
		return "%s" % self.name

class Attachment(TimeStamp):
	
	# Relations
	project = models.ForeignKey(Project)
	user = models.ForeignKey(AUTH_USER_MODEL, related_name="user_fk")
	
	# Fields
	file = models.FileField(upload_to='attachments/')
	
	# Methods
	def __str__(self):
		return "%s" % self.file