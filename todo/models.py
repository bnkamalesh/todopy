from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Todo(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	done = models.BooleanField(default=False)

	def __unicode__(self): # "label" of the object
		return self.title
	def __unicode__(self): # "label" of the object
		return self.description
