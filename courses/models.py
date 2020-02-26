from django.db import models

# Create your models here.
class Course(models.Model):

	availability		=models.CharField(max_length=80)
	coursePictureUrl	=models.CharField(max_length=120)
	credits				=models.CharField(max_length=5)
	endDate 			=models.CharField(max_length=20)
	enrolled  			=models.CharField(max_length=20)
	enrollmentEndDate   =models.CharField(max_length=20)
	examDate			=models.CharField(max_length=20)
	explorerInstructorName=models.CharField(max_length=50)
	featured			=models.CharField(max_length=20)
	instructorInstitute =models.CharField(max_length=80)
	name 				=models.CharField(max_length=50)
	ncCode				=models.CharField(max_length=20)
	nodeCode			=models.CharField(max_length=20)
	openForRegistration =models.CharField(max_length=20)
	startDate			=models.CharField(max_length=20)
	title				=models.CharField(max_length=50)
	url 				=models.CharField(max_length=80)
	weeks   			=models.CharField(max_length=20)


	def __str__(self):

		return self.explorerInstructorName +"  "+self.ncCode