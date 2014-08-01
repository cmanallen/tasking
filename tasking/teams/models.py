from django.db import models
from django.core.urlresolvers import reverse
from utils.models import TimeStamp
from users.models import User

# Create your models here.
class Team(TimeStamp):
	# Table Fields
	name = models.CharField(max_length=255)
	description = models.TextField()

	# Relations
	user_team = models.ManyToManyField(User)

	# Model Methods
	def get_absolute_url(self):
		return reverse('detail-team', kwargs={'pk': self.id})

	def __str__(self):
		return "%s" % self.name