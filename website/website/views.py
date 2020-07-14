from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from website.models import Trade, Asset
import time
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime
import wget
import json
from django.contrib.auth.models import User
import requests

#=============================================================#



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  @get_symbol_summary(str) [LIST]
#  Returns a list of json objects for every traded pair matching 
#  the given ticker

import os.path
import time
import urllib.request
from datetime import datetime
import os.path
def get_trade_json():
	api_url = "https://api.binance.com/api/v3/trades?symbol=BTCUSDT"
	trades = requests.get(api_url)
	trades_json = json.loads(trades.text)

	# Write data to disk #
	#		     #
	#                    #
	now = datetime.now()	
	timestamp = datetime.timestamp(now)
	save_path = 'C:/Users/Admin/Desktop/tl'
	file_name = str(timestamp) + "_tradelist.txt"
	completeName = os.path.join(save_path, file_name)
	f = open(completeName, 'w')
	f.write(trades.text)
	f.close()

	
	
	# Returns json of the last 500 trades
	return trades_json

def get_binance_json(url):
	resp = requests.get(url)
	return json.loads(resp.text)

def get_bookTicker():
	resp = get_binance_json("https://api.binance.com/api/v3/ticker/bookTicker")
	return resp 

def get_price(symbol="BTCUSDT",write=False):
	url = 'https://api.binance.com/api/v3/ticker/price'
	url = url + '?symbol=' + symbol
	resp = requests.get(url)
	js = json.loads(resp.text)
	if write:
		new_asset = Asset(name=js['symbol'], price=js['price'])
		confirm = new_asset.save()
	return js

def invest2(request):
	try:
		symbol = request.GET.get('symbol','LTCBTC')
	except:
		symbol = "LTCBTC"
		pass

	price_json = get_price(symbol,True)

	return HttpResponse(price_json['symbol'] \
	+ " " + price_json['price'])

def get_symbol_summary():
	api_url = 'https://api.binance.com/api/v3/ticker/24hr' 
	pairs = requests.get(api_url)
	parsed_json = json.loads(pairs.text)
	return parsed_json


def write_trades_to_db(js):
	
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

	return


def invest(request):
	context = {}
	pair_listings = get_symbol_summary() #24 hour data
	bt = get_bookTicker()
	context['bookTicker'] = bt
	context['bookTicker_top'] = []
	print(context['bookTicker'])

	for t in bt:
		s = float(t['askPrice']) - float(t['bidPrice'])
		if s>0:
			x = (s/float(t['askPrice'])) * 100
			if (x>1):
				z = t['symbol']
				context['bookTicker_top'].append([z,s,x])
		
	

	for pair in pair_listings:
		pair['priceChangePercent'] = float(pair['priceChangePercent'])
	context['pair_listings'] = pair_listings

	trades_json = get_trade_json()
	context['trades'] = trades_json 
	write_trades_to_db(trades_json)
	context['large_trades'] = []

	for trade in context['trades']:
		if float(trade['qty']) > 0.1:
			context['large_trades'].append(trade)
	context['number_of_large_trades'] = len(context['large_trades'])
		
	print(context['bookTicker'])
	


	#time.sleep(100)
	#return HttpResponseRedirect('/invest')
	#return
	return render(request, 'invest.html', context)
































#-----------------------------------------------------------------
#  Home page

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
	return HttpResponse("about_page")

def shop(request):
	context = { 'data' : 12345 }

	return render(request, 'shop.html', context)
	return HttpResponse("shop")


def contact(request):
	context = { 'data' : 12345 }
	return render(request, 'contact.html', context)
	return HttpResponse("contact")

def account(request):
	context = { 'data' : 12345 }
	return render(request, 'account.html', context)
	return HttpResponse("account")

