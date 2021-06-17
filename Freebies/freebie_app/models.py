from django.db import models

# Create your models here.
class FreebiesPostDb(models.Model):

	name = models.CharField(max_length=100);
	email = models.CharField(max_length=100);
	number = models.CharField(max_length=100);
	program = models.CharField(max_length=100);
	state = models.CharField(max_length=100);
	country = models.CharField(max_length=100);
	tee_size = models.CharField(max_length=10);