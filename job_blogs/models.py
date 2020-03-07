from django.db import models

# Create your models here.
class Job_Blog(models.Model):

	
	image		=models.CharField(max_length=80)
	blog_title	=models.CharField(max_length=150)
	blog_link	=models.CharField(max_length=80)
	read_more	=models.CharField(max_length=80)
	date		=models.CharField(max_length=25)

	def __str__(self):

		return self.blog_title

