from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utils.models import TimeStamp
from projects.models import Project

# Create your models here.
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
		(BUG, 'Bug'),
		(FEATURE, 'Feature'),
	)
	# Relations
	user_task = models.ManyToManyField(User, through='UserTask')
	project = models.ForeignKey(Project, blank=True)
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()
	status = models.IntegerField(choices=STATUS_CHOICES)
	task_type = models.IntegerField(choices=TYPE_CHOICES)
	due = models.DateField()
	# Model methods
	def get_task_comment(self):
		return self.comment_set.all()
	def get_task_user(self):
		return self.usertask_set.all()
	def get_absolute_url(self):
		return reverse('detail-task', kwargs={'pk': self.id})
	# Class meta data
	class Meta:
		ordering = ['-created']

class UserTask(TimeStamp):
	# Relations
	user = models.ForeignKey(User)
	task = models.ForeignKey(Task)
	# Table Fields
	reassigned = models.DateField(null=True)
	completed = models.DateField(null=True)
	removed = models.DateField(null=True)

class Comment(TimeStamp):
	# Relations
	task = models.ForeignKey(Task)
	user = models.ForeignKey(User)
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()

class Image(TimeStamp):
	# Relations
	task = models.ForeignKey(Task)
	# Table Fields
	image = models.ImageField(upload_to='images/')