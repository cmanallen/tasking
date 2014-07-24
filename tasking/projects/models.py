from django.db import models
from utils.models import TimeStamp
from django.contrib.auth.models import User

# Create your models here.
class Project(TimeStamp):
	# Relations
	created_by = models.ForeignKey(User)
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()