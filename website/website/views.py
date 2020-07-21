import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from website.models import Trade, Asset, Trade, Signal

import time
import os
import os.path
import wget
import json
import requests
import urllib.request
# ------------------------------------------------------------ #
#
#
#
#
### API HELPERS ########################################################
########################################################################

TRADE_QTY_THRESHOLD = 1


def get_binance_json(url):
	''' Returns parsed JSON from a binance URL endpoint '''
	resp = requests.get(url)
	return json.loads(resp.text)

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

### URL HOOKS ##########################################################
########################################################################

def get_last_price(request,write=True):
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

	return HttpResponse(new_asset.price)

def trades(request):

	# init vars
	# for now defaults to BTCUSDT
	context = {}
	context['large_trades'] = []
	url = "https://api.binance.com/api/v3/trades?symbol=BTCUSDT"

	# get json trade data & write to db
	trades_json = get_binance_json(url)
	success = write_trades_to_db(trades_json)

	# Fill context & create & write a signal (if needed)
	for trade in trades_json:
		if (float(trade['qty']) > TRADE_QTY_THRESHOLD):
			context['large_trades'].append(trade)
			t = datetime.datetime.now()
			s = Signal(price=trade['price'], 
		       	 qty=trade['qty'], 
			 timestamp=t)
			s.save()
	context['number_of_large_trades'] = len(context['large_trades'])

	# Return HTML
	return render(request, 'invest.html', context)

def invest(request):	

	# init vars
	context = {}
	url = "https://api.binance.com/api/v3/ticker/24hr"
	url2 = "https://api.binance.com/api/v3/ticker/price"

	# Get 24 hour pair listing data
	pair_listings = get_binance_json(url)

	# Get current prices		
	snapshot = get_binance_json(url2)
	
	# Fill context
	for pair in pair_listings:
		pair['priceChangePercent'] = float(pair['priceChangePercent'])
	context['pair_listings'] = pair_listings
	context['snapshot'] = snapshot

	# return HTML
	return render(request, 'invest.html', context)

# STATIC 
# --------------------------------------------------------------------------------- #
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
	t = datetime.today()
	context = { 'data' : 12345, 't':t}

	return render(request, 'shop.html', context)


def contact(request):
	context = { 'data' : 12345 }
	return render(request, 'contact.html', context)

def account(request):
	context = { 'data' : 12345 }
	return render(request, 'account.html', context)



#===============
#================
# ML SECTION
#===============
#================


def insights(request):
	trades = Trade.objects.all()
	context = {'trades': trades}
	
	return render(request, 'insight.html', context)
