from datetime import datetime
import requests, time
import os

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

COUNTER=1

# Signal beggining
print("EasternWeb Project\nver: 0\n")
print(datetime.now())
print("--------------------")

# start script
while COUNTER:
	'''Loops indefinately and gathers market data from easternweb '''

	# get BTC Trade data (500 most recent) and write to db
	print("Sending request to Binance")
	r=requests.get("http://localhost:8000/trades") 
	print("BTC trade-objs > db")

	# get XRP Trade data (500 most recent) and write to db
	print("Sending request to Binance")
	r=requests.get("http://localhost:8000/trades2")
	print("XRP trade-objs > db")

	# Get most recent prices & print to console
	print("Collecting price data")
	print("----")
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

	# Clear console gui every second pass
	COUNTER=COUNTER+1
	if COUNTER==2:
		cls()
		lc=1
		print("BTC PRICE: " + r2.text)
		print("ETH PRICE: " + r3.text)
		print("DASH PRICE: " + r7.text)
		print("KNC PRICE: " + r6.text)
		print("XLM PRICE: " + r5.text)
		print("XRP PRICE: " + r4.text)
		print("DASH PRICE: " + r7.text)
		print("=======================")
