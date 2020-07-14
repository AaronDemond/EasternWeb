from datetime import datetime
import time
import requests

print("Gathering BTC market data")
while True:
	r=requests.get("http://localhost:8000/invest2?symbol=BTCUSDT")
	r=requests.get("http://localhost:8000/invest")
	time.sleep(10)


