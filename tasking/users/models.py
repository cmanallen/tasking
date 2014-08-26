from django.db import models
from django.db.models import Count
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from utils.models import TimeStamp


# Create your models here.
class User(AbstractUser):
	# Fields
	avatar = models.ImageField(upload_to='images/', blank=True, null=True)
	# Methods
	def get_absolute_url(self):
		return reverse('detail-user', kwargs={'pk': self.id})
