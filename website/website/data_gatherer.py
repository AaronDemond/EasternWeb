from datetime import datetime
import time
import requests
#from website.website.models import Signal

print("Gathering BTC market data")
while True:
    print("sending request")
    r=requests.get("http://localhost:8000/trades") #btc
    r=requests.get("http://localhost:8000/trades2") #xrp
    r=requests.get("http://localhost:8000/invest")

    r2=requests.get("http://localhost:8000/get-last-price?symbol=BTCUSDT")
    print("BTC PRICE: " + r2.text)

    r2=requests.get("http://localhost:8000/get-last-price?symbol=ETHUSDT")
    print("ETH PRICE: " + r2.text)

    r2=requests.get("http://localhost:8000/get-last-price?symbol=XRPUSDT")
    print("XRP PRICE: " + r2.text)

    r2=requests.get("http://localhost:8000/get-last-price?symbol=XLMUSDT")
    print("XLM PRICE: " + r2.text)

    r2=requests.get("http://localhost:8000/get-last-price?symbol=KNCUSDT")
    print("KNC PRICE: " + r2.text)

    ##################################################
    print("sleeping")
    time.sleep(1)


