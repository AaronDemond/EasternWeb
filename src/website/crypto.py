from website.models import Signal, Trade
import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from website.models import Trade, Trade, Signal, HistoricalPrice, Candle

import time
import os
import os.path
import wget
import json
import requests
import urllib.request
import datetime, time

class Helper():
	''' General helper functions '''

	def sort(self,signals):
		'''Accepts a queryset or list of signals and returns a
		   list sorted by its quantity
		'''	
		signalList = []
		for s in signals:
			try:
				if s.qty and s.symbol==signals[0].symbol:
					signalList.append(s)
			except:
				pass
		def getQty(x):
			try:
				q=float(x.qty)
			except:
				q=0
			return q
		return signalList.sort(key=getQty,reverse=True)

class SignalHelper():
	''' Signal generation functions '''

	def getPriceChangeAlert(self,price_QS, symbol_str):
		'''Accepts a QuerySet object & symbolpair and writes a price change
		   signal to db if requirements are hit '''

		n = [float(price_QS[0].price), float(price_QS[1].price)]
			# [0] = newer
		p_change = (((n[0] - n[1])/n[1]) * 100)
		if (p_change > 1):
			newSignal = Signal(symbol=symbol_str+" PRICE ALERT")
			s=newSignal.save()
			alert_str= "Price increase alert: " + symbol_str + " " + str(p_change)
			alert_str= alert_str + "\nFrom " + str(n[1]) + " to " + str(n[0])
		if (p_change < 0):
			newSignal = Signal(symbol=symbol_str+" PRICE ALERT")
			s=newSignal.save()
			alert_str= "Price decrease alert: " + symbol_str + " " + str(p_change)
			alert_str= alert_str + "\nFrom " + str(n[1]) + " to " + str(n[0])
		else:
			alert_str = "No major movement: " + symbol_str + " " + str(n[0])
			alert_str= alert_str + "\nFrom " + str(n[1]) + " to " + str(n[0])
		return alert_str

	def generateVolumeSignal(self, trade, symbol_str):
		''' Accepts a trade object & symbolpair and writes a signal 
		   to db if requirements are hit '''

		signal_discovered = False
		if symbol_str == "BTCUSDT":
			if (float(trade.qty) > 1.2):
				signal_discovered=True
		if symbol_str == "ETHUSDT":
			if (float(trade.qty) > 10):
				signal_discovered=True
		if symbol_str == "XRPUSDT":
			if (float(trade.qty) > 100000): 
				signal_discovered=True
		if symbol_str == "KNCUSDT":
			if (float(trade.qty) > 500): 
				signal_discovered=True
		if signal_discovered == True:
			print ("spawning alert")
			newSignal = Signal(symbol=symbol_str,
					qty = str(trade.qty),
					source = "BINANCE",
					signal_type = "volume")
			ns = newSignal.save()
			return True
		return False
