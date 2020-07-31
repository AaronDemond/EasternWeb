from datetime import datetime
from colorama import Fore, Style
import requests, time
import os
SYMBOLPAIRS = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'XLMUSDT', 'KNCUSDT', 'DASHUSDT']
VERSION="0.0"
GREETING="EasternWeb Project \nVersion: "+VERSION+"\n------"

class DataGatherer():
	
	def __init__(self):
		self.symbolpairs=SYMBOLPAIRS
		print(GREETING)


	def gather_priceData(self,symbol='BTCUSDT'):
		r=requests.get("http://localhost:8000/get-last-price?symbol="+symbol)
		return(symbol + " PRICE: " + r.text)

	def gather_tradeData(self,symbol='BTCUSDT'):
		r=requests.get("http://localhost:8000/trades")
		return("BTC trade-objs > db")



def cls():
	os.system('cls' if os.name=='nt' else 'clear')



def __main__():

	dg = DataGatherer()

	while True:	
		print("collecting price data\n\n")
		for s in dg.symbolpairs:
			print(dg.gather_priceData(s))
			print("=========")

		print("sleeping")
		print("###############")
		time.sleep(1)

__main__()
