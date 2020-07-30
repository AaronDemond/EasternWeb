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

TRADE_QTY_THRESHOLD_BTC = 1
TRADE_QTY_THRESHOLD_XRP = 26000


def get_binance_json(url):
	''' Returns parsed JSON from a binance URL endpoint '''
	resp = requests.get(url)
	return json.loads(resp.text)

def write_trades_to_db(js,symbol="BTCUSDT"):
	''' Accepts js (JSON trade data) and writes to db '''	
	for trade in js:
		new_trade = Trade(trade_id = trade['id'], 
		price = trade['price'], 
		qty = trade['qty'], 
		symbol = symbol,
		quoteQty = trade['quoteQty'], 
		time = trade['time'])
		try:
			x = new_trade.save()
		except:
			print("Error saving trade")
	return True

def get_last_price(request):
	''' Returns an HttpResponse, writes the 
	price data to db '''
	try:
		symbol = request.GET.get('symbol','LTCBTC')
	except:
		symbol = "LTCBTC"
		pass

	url = 'https://api.binance.com/api/v3/ticker/price'
	url = url + '?symbol=' + symbol
	resp = requests.get(url)
	js = json.loads(resp.text)
	t = datetime.datetime.now()
	historical_price = HistoricalPrice(
			symbol=js['symbol'], 
			price=js['price'],
			time = t,
			source="Binance",
			)
	confirm = historical_price.save()
	spawn_alert(historical_price,symbol)
	return HttpResponse(historical_price.price)

def spawn_alert(historical_price,symbol):
	hpl = HistoricalPrice.objects.all().order_by("-id")[:10]
	hpl1 = []
	for x in hpl:
		if x.symbol==symbol:
			hpl1.append(x)
	counter=0
	for x in hpl1:
		if (((float(hpl1[0].price - x.price)/x.price)*100)>0.5):
			s = Signal(price=x.price, 
			 timestamp=datetime.datetime.now(),
			 data = "current price:" + str(str(hpl1[0].price) + " previous: "+str(x.price)),
			 symbol=symbol,
			 price_change= ((float(hpl1[0].price - x.price)/x.price)*100),
			)
			s.save()
			print("alert spawned")



def trades(request):
	''' for now defaults to BTCUSDT '''

	context = {}
	context['large_trades'] = []
	url = 'https://api.binance.com'\
	'/api/v3/trades?symbol=BTCUSDT'

	# get json trade data & write to db
	trades_json = get_binance_json(url)
	success = write_trades_to_db(trades_json)

	# Fill context & create & write a 
	# signal (if needed)
	for trade in trades_json:
		if (float(trade['qty']) > TRADE_QTY_THRESHOLD_BTC):
			context['large_trades'].append(trade)
			t = datetime.datetime.now()
			s = Signal(price=trade['price'], 
		       	 qty = trade['qty'], 
			 timestamp=t,
			 symbol="BTCUSDT"
			)
			s.save()
	context['number_of_large_trades'] = len(context['large_trades'])
	return render(request, 'invest.html', context)
def trades2(request):
	''' for now defaults to BTCUSDT '''

	context = {}
	context['large_trades'] = []
	url = 'https://api.binance.com'\
	'/api/v3/trades?symbol=XRPUSDT'

	# get json trade data & write to db
	trades_json = get_binance_json(url)
	success = write_trades_to_db(trades_json)

	# Fill context & create & write a 
	# signal (if needed)
	for trade in trades_json:
		if (float(trade['qty']) > TRADE_QTY_THRESHOLD_XRP):
			context['large_trades'].append(trade)
			t = datetime.datetime.now()
			s = Signal(price=trade['price'], 
		       	 qty = trade['qty'], 
			 timestamp=t,
			 symbol="XRPUSDT"
			)
			s.save()
	context['number_of_large_trades'] = len(context['large_trades'])
	return render(request, 'invest.html', context)
def invest(request):	
	'''Returns general market info'''
	context = {}
	url = "https://api.binance.com/api/v3/ticker/24hr"
	url2 = "https://api.binance.com/api/v3/ticker/price"

	# Get 24 hour pair listing data
	pair_listings = get_binance_json(url)

	# Get current prices		
	snapshot = get_binance_json(url2)
	
	# Fill context and return
	for pair in pair_listings:
		pair['priceChangePercent'] = float(pair['priceChangePercent'])
	context['pair_listings'] = pair_listings
	context['snapshot'] = snapshot

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
	t = datetime.datetime.now()
	context = { 'data' : 12345, 't':t}
	return render(request, 'shop.html', context)


def contact(request):
	context = { 'data' : 12345 }
	return render(request, 'contact.html', context)

def account(request):
	context = { 'data' : 12345 }
	return render(request, 'account.html', context)

def insights(request):
	trades = Trade.objects.all().order_by("-id")[:50000]
	context = {'trades': trades}
	outp =""
	hits=0

	for t in trades:
		if (float(t.qty)  > 5):
			hits=hits+1

	return HttpResponse("todo")


def getCandleData(request):
# returns json
# ex: http://localhost:8000/get-candle-data?symbol=XRPUSDT 

	symbol=request.GET.get('symbol', 'XRPUSDT')
	interval=request.GET.get('interval', '30m')
	st = 1594052883 
	jsondata = get_binance_json('https:' +\
'//api.binance.com/api/v3/klines?symbol=' + symbol +\
'&interval='+interval+'&limit=7')#&startTime=' + str(st))
	writeCandleDataset(jsondata,symbol,'Binance')
	return HttpResponse(jsondata)

def writeCandleDataset(js,s,source_str):
	for candleDataSet in js:
		new_candle = Candle(
		###
		symbol=s,
		source=source_str,
		###
		open_time = candleDataSet[0],
		open_price = candleDataSet[1],
		high_price = candleDataSet[2],
		low = candleDataSet[3],
		close = candleDataSet[4],
		volume = candleDataSet[5],
		close_time = candleDataSet[6],
		quote_asset_volume = candleDataSet[7],
		number_of_trades = candleDataSet[8],
		taker_buy_base_asset_volume = candleDataSet[9],
		taker_buy_quote_asset_volume = candleDataSet[10],
		ignore = candleDataSet[11],
		)
		conf=new_candle.save()
	
		



