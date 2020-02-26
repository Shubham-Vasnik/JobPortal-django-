from django.db import models

# Create your models here.
class  JobDesc(models.Model):
	

	job_type                   =models.CharField(max_length=50)
	country                    =models.CharField(max_length=30)	
	city                       =models.CharField(max_length=50)
	url                        =models.CharField(max_length=50)
	uniq_id                    =models.CharField(max_length=50)
	job_description            =models.TextField(max_length=1000)
	post_date                  =models.CharField(max_length=50)
	company_name               =models.CharField(max_length=50)
	state                      =models.CharField(max_length=50)
	category                   =models.CharField(max_length=50)
	contact_email              =models.EmailField(max_length=50)

	def __str__(self):
		return self.company_name +" "+self.city
