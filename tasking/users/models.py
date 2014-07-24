from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utils.models import TimeStamp

# Create your models here.
class Profile(TimeStamp):
	# Relations
	user = models.OneToOneField(User)
	# Fields
	avatar = models.ImageField(upload_to='images/', blank=True, null=True)

	def get_absolute_url(self):
		return reverse('detail-user', kwargs={'pk': self.id})