from django.db import models

# Create your models here.

class News(models.Model):

	news_title			=models.CharField(max_length=200)
	news_link			=models.CharField(max_length=80)
	date				=models.CharField(max_length=20)
	image				=models.CharField(max_length=80)

	class Meta:
		verbose_name="News"
		verbose_name_plural="News_Blog"


	def __str__(self):
		return self.date+"  news "