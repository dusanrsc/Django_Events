# importing modules and sub-modules
from django.db import models

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=20)
	location = models.CharField(max_length=20)
	description = models.TextField(max_length=25)
	date = models.DateField(max_length=15)
	time = models.TimeField(max_length=15)
	tickets = models.IntegerField()

	def __str__(self):
		return self.title