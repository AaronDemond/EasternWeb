from django.db import models 

import datetime




class HistoricalPrice(models.Model):
	''' Record of the given most recent market price '''

	price = models.FloatField(null=True, blank=True)
	time = models.FloatField(null=True, blank=True)
	source = models.CharField(max_length=1000,null=True, blank=True)

########

class LocalHighHistorical(models.Model):
	pass

class HistoricalBound(models.Model):
	pass

class HistoricalTrend(models.Model):
	pass




class Trade(models.Model):
	''' Record of A trade executed on Binance.com '''

	trade_id = models.FloatField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	qty = models.FloatField(null=True, blank=True)
	quoteQty = models.FloatField(null=True, blank=True)
	time = models.FloatField(null=True, blank=True)
	isBuyerMaker = models.BooleanField(null=True, blank=True)
########


class Signal(models.Model):
	''' Market Signal Model Class
	-------------------------------------------------------
	Signals are created when interesting things happen
	in the market. Such as, a large trade going through.
	These signals should be attached to a delivery 
	pipeline where account owenrs can automatically
	receive them.  '''

	name  = models.CharField(max_length=200,null=True)
	signif  = models.CharField(max_length=200,null=True)
	action_url  = models.CharField(max_length=200,null=True)
	source  = models.CharField(max_length=200,null=True)
	data  = models.CharField(max_length=200,null=True)
	symbol = models.CharField(max_length=200,null=True)
	price = models.CharField(max_length=200,null=True)
	qty = models.CharField(max_length=200,null=True)
	timestamp = models.CharField(max_length=200,null=True)

	# Defines the text str to return on model.name
	def __str__(self):
		s = str(self.qty) + " of BTCUST @ "+ self.price
		return s

class Asset(models.Model):
	name = models.CharField(max_length=201,
		null=True,blank=True)
	price_url = models.CharField(max_length=400,
		 null=True,blank=True)
	price = models.FloatField(null=True, blank=True)




	


