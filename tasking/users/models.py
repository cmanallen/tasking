from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models

from utils.models import TimeStamp


class User(AbstractUser):
	
	# Fields
	avatar = models.ImageField(upload_to='images/', default='images/default-avatar.jpg')
	
	# Methods
	def get_absolute_url(self):
		return reverse('detail-user', kwargs={'pk': self.id})
