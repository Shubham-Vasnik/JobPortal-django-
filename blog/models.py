from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver




class JobPost(models.Model):
	job_title 				= models.CharField(max_length=50, null=False, blank=False)
	job_type				= models.CharField(max_length=50,null=False,blank=False)

	job_description			= models.TextField(max_length=5000, null=False, blank=False)
	url						= models.CharField(max_length=100,null=False,blank=False)
	location				= models.CharField(max_length=40)
	position				= models.CharField(max_length=30,null=False,blank=False)
	date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	contact_email 			= models.EmailField(max_length=60)
	company_name			= models.CharField(max_length=30)

	slug 					= models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.job_title+" "+self.author.username



def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.job_title)

pre_save.connect(pre_save_blog_post_receiver, sender=JobPost)


