from django.db import models
from django.db.models import Count
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
	# Model Methods
	with_tasks = TaskCount()
	objects = models.Manager()
	def __str__(self):
		return "%s" % self.name
