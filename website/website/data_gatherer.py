from datetime import datetime
import time
import requests
#from website.website.models import Signal

print("Gathering BTC market data")
while True:
	print("sending get req")
	r=requests.get("http://localhost:8000/trades")
	r=requests.get("http://localhost:8000/invest")
	r2=requests.get("http://localhost:8000/get-last-price?symbol=BTCUSDT")
	r2=requests.get("http://localhost:8000/get-last-price?symbol=ETHUSDT")
	r2=requests.get("http://localhost:8000/get-last-price?symbol=XRPUSDT")
	r2=requests.get("http://localhost:8000/get-last-price?symbol=XLMUSDT")
	r2=requests.get("http://localhost:8000/get-last-price?symbol=KNCUSDT")
	print("sleeping")
	time.sleep(7)


