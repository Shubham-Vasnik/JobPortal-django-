from django.db import models

# Create your models here.
class ScholarShip(models.Model):

	scholarship_name	= models.CharField(max_length=60)
	scholarship_link	=models.CharField(max_length=80)
	image				=models.CharField(max_length=80)
	details				=models.CharField(max_length=200)
	apply_data			=models.CharField(max_length=25)
	time				=models.CharField(max_length=25)


	def __str__(self):
		return self.scholarship_name
