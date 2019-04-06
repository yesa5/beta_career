from django.db import models

# Create your models here.
class Report(models.Model):
	
	title = models.CharField(max_length = 100)
	body = models.TextField()
	mark = models.IntegerField(default=0) 
	date = models.DateTimeField(auto_now_add = True)