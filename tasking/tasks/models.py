from django.db import models
from django.core.urlresolvers import reverse
from users.models import User
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
		(BUG, 'Issue'),
		(FEATURE, 'Request'),
	)	
	
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()
	status = models.IntegerField(choices=STATUS_CHOICES)
	task_type = models.IntegerField(choices=TYPE_CHOICES)
	due = models.DateField()
	created_by = models.ForeignKey(User, related_name='creator')
	
	# Relations
	user_task = models.ManyToManyField(User)
	project = models.ForeignKey(Project, blank=True)
	
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
	user = models.ForeignKey(User)
	# Table Fields
	body = models.TextField()

	def __str__(self):
		return self.body

class Image(TimeStamp):
	# Relations
	task = models.ForeignKey(Task)
	# Table Fields
	image = models.ImageField(upload_to='images/')