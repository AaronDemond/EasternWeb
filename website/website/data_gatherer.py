from datetime import datetime
import time
import requests
#from website.website.models import Signal

print("Gathering BTC market data")
while True:
    print("sending get req")
    r=requests.get("http://localhost:8000/trades")
    r=requests.get("http://localhost:8000/invest")
    print("sleeping")
    time.sleep(10)


