from django.db import models


class About(models.Model):
	Image = models.ImageField(upload_to = 'upload/images')
	Title = models.CharField(max_length = 30)
	desc = models.CharField(max_length = 200)


	def __str__(self):
		return self.Title