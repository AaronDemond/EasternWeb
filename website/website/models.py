from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)

class Asset(models.Model):
	name = models.CharField(max_length=201,null=True,blank=True)
	price_url = models.CharField(max_length=400, null=True,blank=True)
	price = models.FloatField(null=True, blank=True)


class Trade(models.Model):
	trade_id = models.FloatField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	qty = models.FloatField(null=True, blank=True)
	quoteQty = models.FloatField(null=True, blank=True)
	time = models.FloatField(null=True, blank=True)


class Signal(models.Model):
	name  = models.CharField(max_length=200,null=True)
	signif  = models.CharField(max_length=200,null=True)
	action_url  = models.CharField(max_length=200,null=True)
	source  = models.CharField(max_length=200,null=True)
	data  = models.CharField(max_length=200,null=True)
	symbol = models.CharField(max_length=200,null=True)
	price = models.CharField(max_length=200,null=True)
	qty = models.CharField(max_length=200,null=True)
	timestamp = models.CharField(max_length=200,null=True)

	def __str__(self):
		import datetime
		s = str(self.qty) + " of of BTCUST "
		return s


#try to influence other bots and profit off it






class EasternWebAccount(models.Model):
	username = models.CharField(max_length=200,null=True)
	password = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	join_date = models.DateField(auto_now=False, 
		auto_now_add=True,blank=True,null=True)

	
class GC(models.Model):
	account = models.ForeignKey(EasternWebAccount, on_delete=models.CASCADE,null=True,blank=True)
	number = models.CharField(max_length=200)
	active = models.BooleanField(default=False)
	balance = models.FloatField(null=True, blank=True)

class assetpair0(models.Model):
	name = models.CharField(max_length=200)
	pct_change = models.FloatField(null=True, blank=True)
	daily_open =  models.FloatField(null=True, blank=True)
	last =  models.FloatField(null=True, blank=True)
	


