from django.db import models
from django.db.models import Count
from django.core.urlresolvers import reverse
from utils.models import TimeStamp
from users.models import User

# Model Managers
class TaskCount(models.Manager):
	def get_query_set(self):
		return super(TaskCount, self).get_query_set().annotate(tasks=Count('task'))

# Create your models here.
class Project(TimeStamp):
	# Relations
	created_by = models.ForeignKey(User)
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()
	# Queries
	with_tasks = TaskCount()
	objects = models.Manager()
	# Model Methods
	def get_absolute_url(self):
		return reverse('detail-project', kwargs={'pk': self.id})

	def __str__(self):
		return "%s" % self.name
