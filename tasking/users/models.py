from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models

from utils.models import TimeStamp


class User(AbstractUser):
	
	# Fields
<<<<<<< HEAD
	avatar = models.ImageField(upload_to='images/', blank=True, null=True)
	
=======
	avatar = models.ImageField(upload_to='images/', default='images/default-avatar.jpg')
>>>>>>> c6656b17ba60ef73a0f37768c68dc2abfdd01366
	# Methods
	def get_absolute_url(self):
		return reverse('detail-user', kwargs={'pk': self.id})
