from django.db import models

class documentsPage(models.Model):
	title=models.CharField(max_length=140)
	body=models.TextField()

	def __str__(self):
		return self.title
# Create your models here.
