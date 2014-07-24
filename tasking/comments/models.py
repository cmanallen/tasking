from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utils.models import TimeStamp

# Create your models here.
class Comment(TimeStamp):
	# Relations
	user = models.ForeignKey(User)
	task = models.ForeignKey(Task)
	# Fields
	body = models.TextField()