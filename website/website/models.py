from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)

class EasternWebAccount(models.Model):
	username = models.CharField(max_length=200,null=True)
	password = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	join_date = models.DateField(auto_now=False, auto_now_add=True,blank=True,null=True)

	
class GC(models.Model):
	account = models.ForeignKey(EasternWebAccount, on_delete=models.CASCADE,null=True,blank=True)
	number = models.CharField(max_length=200)
	active = models.BooleanField(default=False)
	balance = models.FloatField(null=True, blank=True)

