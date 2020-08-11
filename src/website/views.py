import time
from website.crypto import SignalHelper
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

TRADE_QTY_THRESHOLD_BTC = 10
TRADE_QTY_THRESHOLD_XRP = 26000
#--------------------------------------------
BINANCE_KLINES_URL = 'https://api.binance.com/api/v3/klines'
#    takes symbol&interval
BINANCE_TICKER_URL = 'https://api.binance.com/api/v3/ticker/price'
BINANCE_TRADES_URL = 'https://api.binance.com/api/v3/trades'
# Singal pair if symbol is passed otherwise list
#-----------------------------------------------

BINANCE_24HR_SNAPSHOT_url = "https://api.binance.com/api/v3/ticker/24hr"
# pair list

def trades_from_json(json,symbol="NONE",source='BINANCE'):
	''' Accepts json trade data and writes to db '''	

	tradelist = []
	for trade in json:
		ibm=False
		try:
			if trade['isBuyerMaker']=='true': ibm=True
		except:
			pass
		new_trade = Trade(trade_id = trade['id'], 
			isBuyerMaker=ibm,
			price = trade['price'], 
			qty = trade['qty'], 
			source=source,
			symbol = symbol,
			quoteQty = trade['quoteQty'], 
			time = trade['time'])

		tradelist.append(new_trade)
	return tradelist

def get_binance_json(url):
	''' Returns parsed JSON from a binance URL endpoint '''
	resp = requests.get(url)
	return json.loads(resp.text)

from website.crypto import SignalHelper
def __get_last_price(request):
	''' takes url param "symbol" and writes price / possible signal to db '''

	symbol_str = request.GET.get('symbol','LTCBTC')
	url_str = BINANCE_TICKER_URL + '?symbol=' + symbol_str
	price_json = json.loads(requests.get(url_str).text)
	timestamp_str = datetime.datetime.now().timestamp()
	sh = SignalHelper()

	recent_prices_QS = HistoricalPrice.objects.filter(symbol__contains=symbol_str)
	recent_prices_QS = recent_prices_QS.order_by("-id")[:2]

	historicalPrice = HistoricalPrice(
			symbol=symbol_str, 
			price=price_json['price'],
			time = timestamp_str,
			source="Binance",
			).save()

	priceChangeAlert_str = sh.getPriceChangeAlert(recent_prices_QS, symbol_str)	

	return HttpResponse(priceChangeAlert_str)	

def trades(request):
	''' /trades?symbol[symbol] '''
	''' writes trades / possible signal to a database and returns write/fail data '''
	''' rendered by /templates/invest.html '''

	symbol_str = request.GET.get('symbol','')
	apiurl_str = BINANCE_TRADES_URL + '?symbol=' + symbol_str
	sh = SignalHelper()
	
	tradelist = trades_from_json(json=get_binance_json(apiurl_str),
				symbol=symbol_str)

	for t in tradelist:
		if sh.generateVolumeSignal(t,symbol_str):
			print ("Volume signal generated")
	return render(request, 'invest.html', {'data': tradelist})

def invest(request):	
	'''Returns general market info'''

	context={}
	context['pair_listings'] = get_binance_json(BINANCE_TICKER_URL)
	context['snapshot'] = get_binance_json(BINANCE_24HR_SNAPSHOT_url)
	return render(request, 'invest.html', context)

def index(request):
	''' Home page '''

	context = { }
	try:
		value= request.POST['email']
		user = User.objects.create_user(value, value, '12345')
		user.save()
	except:
		value = -1
	return render(request, 'index.html', context)

def insights(request):
	'''returns useful crypto info'''
	symbol_str = request.GET.get('symbol','BTCUSDT')
	qty = request.GET.get('sig_qty','10')
	qty=int(qty)
	signals = Signal.objects.filter(symbol__contains=symbol_str).order_by("-id")[:qty]

	print ("test")
	historicalPrices = HistoricalPrice.objects.all().order_by("-time")[:10]
	l=[]
	for h in historicalPrices:
		l.append(h)
	context = { "test" : l, 'signals' : signals }

	return render(request, 'insight.html', context)

def getCandleData(request):
	''' Show candle data in the browser '''
	
	symbol=request.GET.get('symbol', 'BTCUSDT')
	interval=request.GET.get('interval', '30m')
	jsondata = get_binance_json(BINANCE_KLINES_URL+"?symbol="+symbol+"&interval=30m")
	writeCandleDataset(jsondata,symbol,'Binance')
	return HttpResponse(jsondata)

def writeCandleDataset(candleDataSetListJSON,__symbol,__source):
	''' accepts a list of kline data in json and writes it to db '''

	for candleDataSet in candleDataSetListJSON:
		new_candle = Candle(
		symbol=__symbol,
		source=__source,
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
		ignore = candleDataSet[11])
		conf=new_candle.save()
		# candle is now saved. Data format from Binance.
	return True
