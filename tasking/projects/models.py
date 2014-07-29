from django.db import models
from utils.models import TimeStamp
from users.models import User

# Create your models here.
class Project(TimeStamp):
	# Relations
	created_by = models.ForeignKey(User)
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()
	# Model Methods
	def __str__(self):
		return "%s" % self.name