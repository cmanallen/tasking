from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utils.models import TimeStamp

# Create your models here.
class Profile(TimeStamp):
	# Relations
	user = models.OneToOneField(User)
	# Fields
	first = models.CharField(max_length=255, blank=True)
	last = models.CharField(max_length=255, blank=True)
	avatar = models.ImageField(upload_to='images/', blank=True, null=True)