from django.db import models


class Portofolio(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField(max_length=500)
	image = models.ImageField(upload_to='images/')
	url = models.URLField(max_length=200, default='https://redianmarku.herokuapp.com')

	def __str__(self):
		return self.title
