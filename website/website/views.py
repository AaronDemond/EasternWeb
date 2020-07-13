from django.shortcuts import render
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
def get_trade_json():
	api_url = "https://api.binance.com/api/v3/trades?symbol=BTCUSDT"
	trades = requests.get(api_url)
	trades_json = json.loads(trades.text)
	return trades_json

def get_symbol_summary():
	api_url = 'https://api.binance.com/api/v3/ticker/24hr' 
	pairs = requests.get(api_url)
	parsed_json = json.loads(pairs.text)
	return parsed_json


#	@__add_openLastDiff__
#	add the attribute openLastDiff which is the difference
#	between the assets most recent traded price and its opening
#	ticker price


def invest(request):
	context = {}
	pair_listings = get_symbol_summary() #24 hour data

	for pair in pair_listings:
		pair['priceChangePercent'] = float(pair['priceChangePercent'])
	context = {'pair_listings': pair_listings}

	trades_json = get_trade_json()
	context['trades'] = trades_json 
	context['large_trades'] = []

	for trade in context['trades']:
		if float(trade['qty']) > 0.1:
			context['large_trades'].append(trade)
	context['number_of_large_trades'] = len(context['large_trades'])
		
	



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

