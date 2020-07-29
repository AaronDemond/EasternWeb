from django.db import models 

import datetime




class HistoricalPrice(models.Model):
	''' Record of a crypto market price '''

	price = models.FloatField(null=True, blank=True)
	time = models.CharField(max_length=1000,null=True, blank=True)
	symbol = models.CharField(max_length=1000,null=True, blank=True)
	source = models.CharField(max_length=1000,null=True, blank=True)

	def __str__(self):
		return (self.symbol + " " + str(self.price))

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
	symbol = models.CharField(max_length=200,null=True, blank =True)
	time = models.FloatField(null=True, blank=True)
	isBuyerMaker = models.BooleanField(null=True, blank=True)


class Signal(models.Model):
	''' Market Signal Model Class
	-----------------------------
	'''

	name  = models.CharField(max_length=200,null=True)
	signif  = models.CharField(max_length=200,null=True)
	action_url  = models.CharField(max_length=200,null=True)
	source  = models.CharField(max_length=200,null=True)
	data  = models.CharField(max_length=200,null=True)
	symbol = models.CharField(max_length=200,null=True)
	price = models.CharField(max_length=200,null=True)
	qty = models.CharField(max_length=200,null=True)
	timestamp = models.CharField(max_length=200,null=True)
	price_change = models.CharField(max_length=200,null=True)

	# Defines the text str to return on model.name
	def __str__(self):
		s = str(self.qty) + " of BTCUST @ "+ self.price
		return s





	


