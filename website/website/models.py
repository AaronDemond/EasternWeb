import datetime
from django.db import models 

'''
class Candle:                 kline data from Binance.com
class HistoricalBound.........price bound data from Binance.com
class HistoricalPrice:        crypto market price data
class HistoricalTrend.........confirmed historal movement
class Signal:                 Market signals
class Trade(models.Model):....trades executed on Binance.com
'''

class Candle(models.Model):

	open_time = models.CharField(max_length=200,null=True, blank =True)
	open_price = models.CharField(max_length=200,null=True, blank =True)
	high_price = models.CharField(max_length=200,null=True, blank =True)
	low = models.CharField(max_length=200,null=True, blank =True)
	source = models.CharField(max_length=1000,null=True, blank=True)
	close = models.CharField(max_length=200,null=True, blank =True)
	volume = models.CharField(max_length=200,null=True, blank =True)
	close_time = models.CharField(max_length=200,null=True, blank =True)
	quote_asset_volume = models.CharField(max_length=200,null=True, blank =True)
	number_of_trades = models.CharField(max_length=200,null=True, blank =True)
	taker_buy_base_asset_volume = models.CharField(max_length=200,null=True, blank =True)
	taker_buy_quote_asset_volume = models.CharField(max_length=200,null=True, blank =True)
	ignore = models.CharField(max_length=200,null=True, blank =True)
	symbol = models.CharField(max_length=200,null=True, blank =True)


	def __str__(self):
		return(self.symbol)

class HistoricalBound(models.Model):
	pass

class HistoricalPrice(models.Model):

	price = models.FloatField(null=True, blank=True)
	time = models.CharField(max_length=1000,null=True, blank=True)
	symbol = models.CharField(max_length=1000,null=True, blank=True)
	source = models.CharField(max_length=1000,null=True, blank=True)
	avg_price = models.CharField(max_length=200,null=True, blank =True)

	def __str__(self):
		return (self.symbol + " " + str(self.price))

class HistoricalTrend(models.Model):
	pass

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
	price_change = models.CharField(max_length=200,null=True)
	total_quote = models.CharField(max_length=200,null=True)

	def __str__(self):
		try:
			if self.qty:
				return("buy of " + self.qty + " " +self.symbol + " at " + self.price)
			if not self.data:
				return(self.symbol)
			else:
				return(self.symbol + " " + self.data)
		except:
			return ("NO NAME")

class Trade(models.Model):

	trade_id = models.FloatField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	qty = models.FloatField(null=True, blank=True)
	quoteQty = models.FloatField(null=True, blank=True)
	symbol = models.CharField(max_length=200,null=True, blank =True)
	source = models.CharField(max_length=1000,null=True, blank=True)
	time = models.FloatField(null=True, blank=True)
	isBuyerMaker = models.BooleanField(null=True, blank=True)

	def __str__(self):
		if self.symbol:
			return(self.symbol)
		else:
			return("NO SYMBOL GIVEN likely btc")
