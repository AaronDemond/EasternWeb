
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

from website.crypto import Helper
def write_trades_to_db(__json,__symbol="NONE",__source='BINANCE'):
	''' Accepts js (JSON trade data) and writes to db '''	

	for trade in __json:
		ibm=False
		try:
			if trade['isBuyerMaker']=='true': ibm=True
		except:
			pass
		new_trade = Trade(trade_id = trade['id'], 
			isBuyerMaker=ibm,
			price = trade['price'], 
			qty = trade['qty'], 
			source=__source,
			symbol = __symbol,
			quoteQty = trade['quoteQty'], 
			time = trade['time'])
		tradeWritten = new_trade.save()
	return True





def get_binance_json(url):
	''' Returns parsed JSON from a binance URL endpoint '''
	resp = requests.get(url)
	return json.loads(resp.text)


def __get_last_price(request):
	''' Returns an HTML formated string of             '''
	'''  the given ticker                              '''
	'''  market price                                  '''

	symbol = request.GET.get('symbol','LTCBTC')
	url = BINANCE_TICKER_URL + '?symbol=' + symbol
	__json = json.loads(requests.get(url).text)
	__time = datetime.datetime.now()

	historical_price = HistoricalPrice(
			symbol=__json['symbol'], 
			price=__json['price'],
			time = __time,
			source="Binance",
			)
	confirm = historical_price.save()
	return HttpResponse(historical_price.price)


def __get_big_trades__(symbol):
	trades = Trade.objects.all().order_by("-id")[:10000]
	trade_list = []
	for t in trades:
		if (t.symbol==symbol and float(t.qty)>0):
			 trade_list.append(t)
	return trade_list

def __spawnTradeSignal(symbol,trades):
	for t in trades:
		s = Signal(symbol=symbol,qty=t.qty)
		s.save
	


	

def trades(request):
	''' /trades?symbol[symbol] '''
	''' writes trades to a database and returns write/fail data '''
	''' rendered by /templates/invest.html '''

	__symbol__ = request.GET.get('symbol','LTCBTC')
	__apiurl__ = BINANCE_TRADES_URL+'?symbol='+__symbol__

	
	tradesWritten = write_trades_to_db(__json=get_binance_json(__apiurl__),__symbol=__symbol__)

	recent_trades=Trade.objects.all().order_by("-id")[:10000]
	for x in recent_trades:
		if float(x.qty>1):
			if x.symbol=="BTCUSDT":
				s=Signal(symbol="BTCUSDT",qty=x.qty,price=x.price)
				success=s.save()
			if x.symbol=="ETHUSDT":
				if float(x.qty>1):
					s=Signal(symbol="ETHUSDT",qty=x.qty,price=x.price)
					success=s.save()
			if x.symbol=="XRPUSDT":
				if float(x.qty>10000):
					s=Signal(symbol="XRPUSDT",qty=x.qty,price=x.price)
					success=s.save()
			


	return render(request, 'invest.html', {'data':tradesWritten})


def invest(request):	
	'''Returns general market info'''
	context={}
	context['pair_listings'] = get_binance_json(BINANCE_TICKER_URL)
	context['snapshot'] = get_binance_json(BINANCE_24HR_SNAPSHOT_url)
	return render(request, 'invest.html', context)


def index(request):
	''' Home page '''
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
	'''returns useful crypto info'''

	from website.crypto import SignalHelper
	sh = SignalHelper()
	bt=sh.getBigTrades(symbol="BTCUSDT", tradelist=[t for t in Trade.objects.all().order_by("-id")[:100000]], qty_min = 10)
	context={'bt':bt}

	# return rendered template
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
	

