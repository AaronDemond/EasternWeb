from datetime import datetime
import requests, time
import os

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

lc=0
while True:
	lc=lc+1
	'''Loops indefinately and gathers market data from easternweb '''

	# Signal beggining
	print("Collecting trade data")

	# get BTC Trade data (500 most recent) and write to db
	r=requests.get("http://localhost:8000/trades") 
	print("BTC trade-objs > db")

	# get XRP Trade data (500 most recent) and write to db
	r=requests.get("http://localhost:8000/trades2")
	print("XRP trade-objs > db")

	# Get most recent prices & print to console
	print("Collecting price data")
	r2=requests.get("http://localhost:8000/get-last-price?symbol=BTCUSDT")
	print("BTC PRICE: " + r2.text)
	r3=requests.get("http://localhost:8000/get-last-price?symbol=ETHUSDT")
	print("ETH PRICE: " + r3.text)
	r4=requests.get("http://localhost:8000/get-last-price?symbol=XRPUSDT")
	print("XRP PRICE: " + r4.text)
	r5=requests.get("http://localhost:8000/get-last-price?symbol=XLMUSDT")
	print("XLM PRICE: " + r5.text)
	r6=requests.get("http://localhost:8000/get-last-price?symbol=KNCUSDT")
	print("KNC PRICE: " + r6.text)
	r7=requests.get("http://localhost:8000/get-last-price?symbol=DASHUSDT")
	print("DASH PRICE: " + r7.text)

	# Sleep
	print("sleeping")
	print("=====================")
	time.sleep(1)

	# Clear console gui
	if lc==1:
		cls()
		lc=0
		print("BTC PRICE: " + r2.text)
		print("ETH PRICE: " + r3.text)
		print("DASH PRICE: " + r7.text)
		print("KNC PRICE: " + r6.text)
		print("XLM PRICE: " + r5.text)
		print("XRP PRICE: " + r4.text)
		print("DASH PRICE: " + r7.text)
		print("=======================")
