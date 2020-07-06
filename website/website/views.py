from django.shortcuts import render
import time
import os
from django.http import HttpResponse, HttpResponseRedirect
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
		time_stamp = datetime.utcnow().timestamp()	
	except:	
		summary_filename = wget.download(summary)
		time_stamp = datetime.utcnow().timestamp()	
		summary_file = open(summary_filename, 'r')
	
	parsed_json = json.loads(summary_file.read())
	summary_file.close()
	#os.rename('24hr', str(time_stamp))

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

def return_highest_spread(asset_group):

	x ={}
	highest = (asset_group[0],0)
	for pair in asset_group:

		#see if you can access
		try:
			test=pair['diff_percent']
		except:
			pair['diff_percent']=0

		if pair['diff_percent'] > highest[1]:
			highest = (pair["symbol"],pair['diff_percent'])
			
	
	return(highest)
		




def invest(request):
	#get data
	xlm = get_symbol_summary("XLM")
	eth = get_symbol_summary("ETH")
	xrp = get_symbol_summary("XRP")

	context = {'assets': [xlm, eth, xrp]}

	#add diff attribute
	for asset in context['assets']:
		__add_openLastDiff__(asset)
	
	
	#construct context variable
	if "True" in request.GET['xlm']:
		h = return_highest_spread(xlm)

	if "True" in request.GET['eth']:
		h = return_highest_spread(eth)

	if "True" in request.GET['xrp']:
		h = return_highest_spread(xrp)
	

	context['highest_spread'] = h


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

