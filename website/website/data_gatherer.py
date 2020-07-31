from datetime import datetime
from colorama import Fore, Style
import requests, time
import os
SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'XLMUSDT', 'KNCUSDT', 'DASHUSDT']

class DataGatherer():
	def cls(self):
		os.system('cls' if os.name=='nt' else 'clear')

	
	def __init__(self):
		print("EasternWeb Project\nver: 0\n")
		print(datetime.now())
		print("--------------------")
		print(Fore.BLUE + "Hello World")


	def gather_priceData(self,symbol='BTCUSDT'):
		r=requests.get("http://localhost:8000/get-last-price?symbol="+symbol)
		print(symbol + " PRICE: " + r.text)

	def gather_tradeData(self,symbol='BTCUSDT'):
		r=requests.get("http://localhost:8000/trades")
		print("BTC trade-objs > db")


