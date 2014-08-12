from django.db import models
from django.core.urlresolvers import reverse
from utils.models import TimeStamp
from projects.models import Project
from teams.models import Team

from django.conf import settings
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class TaskManager(models.Manager):
	def get_project_tasks(self, project_id):
		return Task.objects.filter(project = project_id)

	def get_user_tasks(self, user_id):
		return Task.objects.filter(user_task = user_id)

	def get_team_tasks(self, team_id):
		return Task.objects.filter(team = team_id)

class Task(TimeStamp):
	# Choices
	OPEN = 0
	CLOSED = 1
	LOCKED = 2
	STATUS_CHOICES = (
		(OPEN, 'Open'),
		(CLOSED, 'Closed'),
		(LOCKED, 'Locked'),
	)
	BUG = 0
	FEATURE = 1
	TYPE_CHOICES = (
		(BUG, 'Issue'),
		(FEATURE, 'Request'),
	)
	LOW = 0
	NORMAL = 1
	HIGH = 2
	CRITICAL = 3
	PRIORITY_CHOICES = (
		(LOW, 'Low'),
		(NORMAL, 'Normal'),
		(HIGH, 'High'),
		(CRITICAL, 'Critical'),
	)
	
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()
	status = models.IntegerField(choices=STATUS_CHOICES, default=0)
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
	task_type = models.IntegerField(choices=TYPE_CHOICES)
	due = models.DateField()
	created_by = models.ForeignKey(AUTH_USER_MODEL, related_name='creator')
	
	# Relations
	user_task = models.ManyToManyField(AUTH_USER_MODEL)
	project = models.ForeignKey(Project, null=True, blank=True, default=None)
	team = models.ForeignKey(Team, null=True, blank=True, default=None)

	# Manager
	objects = TaskManager()
	
	# Model methods
	def get_task_comment(self):
		return self.comment_set.all()

	def get_task_user(self):
		return self.usertask_set.all()

	def get_absolute_url(self):
		return reverse('detail-task', kwargs={'pk': self.id})

	def __str__(self):
		return "%s" % self.name
	
	# Class meta data
	class Meta:
		ordering = ['-created']

class Comment(TimeStamp):
	# Relations
	task = models.ForeignKey(Task)
	user = models.ForeignKey(AUTH_USER_MODEL)
	# Table Fields
	body = models.TextField()

	def __str__(self):
		return self.body

class Image(TimeStamp):
	# Relations
	task = models.ForeignKey(Task)
	# Table Fields
	image = models.ImageField(upload_to='images/')