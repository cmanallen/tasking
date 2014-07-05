from django.db import models
from utils.models import TimeStamp

# Create your models here.
class Project(TimeStamp):
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()