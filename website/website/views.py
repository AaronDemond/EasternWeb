from django.shortcuts import render
import os
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import wget
import json
from django.contrib.auth.models import User

#=============================================================#



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  @get_symbol_summary(str) [LIST]
#  Returns a list of json objects for every traded pair matching 
#  the given ticker
def get_symbol_summary(ticker):
	summary = 'https://api.binance.com/api/v3/ticker/24hr' 
	try:
		summary_file = open('24hr', 'r')
	except:	
		summary_filename = wget.download(summary)
		summary_file = open(summary_filename, 'r')
	
	parsed_json = json.loads(summary_file.read())
	summary_file.close()
	os.remove('24hr')

	pair_listings = []
	for symbol in parsed_json:
		SYMBOL_STR = symbol['symbol']

		if SYMBOL_STR.__contains__(ticker):
			pair_listings.append(symbol)
	return pair_listings

#	@__add_openLastDiff__
#	add the attribute openLastDiff which is the difference
#	between the assets most recent traded price and its opening
#	ticker price
def __add_openLastDiff__(assetpairlist):
	for pair in assetpairlist:
		pair['diff'] = float(pair['lastPrice']) - float(pair['openPrice'])
		try:
			pair['diff_percent'] = float(pair['diff']) / float(pair['openPrice'])
		except:
			pass
	return 




def get_asset_data():
		return [xlm,eth,xrp]






def invest(request):
	#get data
	xlm = get_symbol_summary("XLM")
	eth = get_symbol_summary("ETH")
	xrp = get_symbol_summary("XRP")
	
	#construct context variable
	context = {'assets': [xlm, eth, xrp]}
	
	#add diff attribute
	for asset in context['assets']:
		__add_openLastDiff__(asset)

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

