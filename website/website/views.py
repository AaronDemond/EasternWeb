from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from website.models import Trade, Asset

import time
import os
import os.path
import wget
import json
import requests
import urllib.request
# ------------------------------------------------------------ #



### API HELPERS ################
################################


def get_binance_json(url):
	''' Returns parsed JSON from a binance URL endpoint '''
	resp = requests.get(url)
	return json.loads(resp.text)



def get_last_price(request):
	''' Returns an HttpResponse, writes the price data to db '''
	''' looks for "symbol" get parameter, defaults to LTCBTC '''
	try:
		symbol = request.GET.get('symbol','LTCBTC')
	except:
		symbol = "LTCBTC"
		pass

	url = 'https://api.binance.com/api/v3/ticker/price'
	url = url + '?symbol=' + symbol
	resp = requests.get(url)
	js = json.loads(resp.text)
	if write:
		new_asset = Asset(name=js['symbol'], price=js['price'])
		confirm = new_asset.save()

	return HttpResponse(price_json['symbol'] \
	+ " " + price_json['price'])



def write_trades_to_db(js):
	''' Accepts js (JSON trade data) and writes to db '''
	
	for trade in js:

		new_trade = Trade(trade_id = trade['id'], 
		price = trade['price'], 
		qty = trade['qty'], 
		quoteQty = trade['quoteQty'], 
		time = trade['time'])
		try:
			x = new_trade.save()
		except:
			print("Error saving trade")

	return True




### Url Hooks ##################
################################

def trades(request):
	
	context = {}
	trades_json = get_binance_json("https://api.binance.com/api/v3/trades?symbol=BTCUSDT")
	success = write_trades_to_db(trades_json)
	context['large_trades'] = []

	for trade in trades_json:
		if float(trade['qty']) > 0.1:
			context['large_trades'].append(trade)
	context['number_of_large_trades'] = len(context['large_trades'])
		
	
	return render(request, 'invest.html', context)

def invest(request):
	context = {}
	pair_listings = get_binance_json("https://api.binance.com/api/v3/ticker/24hr")
		
	

	for pair in pair_listings:
		pair['priceChangePercent'] = float(pair['priceChangePercent'])
	context['pair_listings'] = pair_listings

	return render(request, 'invest.html', context)



def index(request):
	context = { 'data' : 12345 }
	try:
		value= request.POST['email']
		user = User.objects.create_user(value, value, '12345')
		user.save()
	except:
		value = -1
	return render(request, 'index.html', context)


def about(request):
	context = { 'data' : 12345 }

	return render(request, 'about.html', context)

def shop(request):
	context = { 'data' : 12345 }

	return render(request, 'shop.html', context)


def contact(request):
	context = { 'data' : 12345 }
	return render(request, 'contact.html', context)

def account(request):
	context = { 'data' : 12345 }
	return render(request, 'account.html', context)

