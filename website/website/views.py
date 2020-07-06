from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import wget
import json
from django.contrib.auth.models import User

#=====================================

def get_xlm_dict():

	now = datetime.now()
	depth = 'https://api.binance.com/api/v3/depth?symbol=BTCUSDT'
	trades = 'https://api.binance.com/api/v3/trades?symbol=BTCUSDT'
	trades2 = 'https://api.binance.com/api/v3/aggTrades?symbol=BTCUSDT'
	summary = 'https://api.binance.com/api/v3/ticker/24hr' 


	# wget returns the name of the file storing returned data #
	#-------------------------------------------------------- #

	##depth_filename = wget.download(depth)
	##trades_filename = wget.download(trades)
	#summary_filename = wget.download(summary)
	
	import os
	try:
		wget.download(summary)
	except:	
		pass

	summary_file = open('24hr', 'r')
	parsed_json = json.loads(summary_file.read())
	summary_file.close()
	os.remove('24hr')


	#store the pairs (XLM) we care about
	pair_listings = []
	for symbol in parsed_json:
		SYMBOL_STR = symbol['symbol']

		if SYMBOL_STR.__contains__('XLMUSDT'):
			pair_listings.append(symbol)

		if SYMBOL_STR.__contains__('XLMUSDC'):
			pair_listings.append(symbol)

		if SYMBOL_STR.__contains__('XLMTUSD'):
			pair_listings.append(symbol)
		if SYMBOL_STR.__contains__('XLMETH'):
			pair_listings.append(symbol)

		if SYMBOL_STR.__contains__('XLMBTC'):
			pair_listings.append(symbol)

		if SYMBOL_STR.__contains__('XLMBNB'):
			pair_listings.append(symbol)


	return(pair_listings)



#================================
def index(request):
	context = { 'data' : 12345 }
	try:
		value= request.POST['email']
		user = User.objects.create_user(value, value, '12345')
		user.save()
	except:
		value = -1
	return render(request, 'index.html', context)

def invest(request):
	context = { 'data' : 12345 }
	xlm = get_xlm_dict()
	sym=''
	for x in xlm:
		sym = x['symbol']
		sym = sym[:3]+ ' ' + sym[3:]
		x['symbol'] = sym
	
	context['xlm'] = xlm
	
	return render(request, 'invest.html', context)
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

