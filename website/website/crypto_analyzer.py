from datetime import datetime
import wget
import json



now = datetime.now()
depth = 'https://api.binance.com/api/v3/depth?symbol=BTCUSDT'
trades = 'https://api.binance.com/api/v3/trades?symbol=BTCUSDT'
trades2 = 'https://api.binance.com/api/v3/aggTrades?symbol=BTCUSDT'
summary = 'https://api.binance.com/api/v3/ticker/24hr' 


# wget returns the name of the file storing returned data #
#-------------------------------------------------------- #

##depth_filename = wget.download(depth)
##trades_filename = wget.download(trades)
#summary_filename = wget.download(summary)

#wget.download(summary)

#open the file, read it, and parse it into json
summary_file = open('24hr', 'r')
parsed_json = json.loads(summary_file.read())


pair_listings = []
x=0
for symbol in parsed_json:
	SYMBOL_STR = symbol['symbol']

	if SYMBOL_STR.__contains__('XLMUSDT'):
		pair_listings.append(symbol)

	if SYMBOL_STR.__contains__('XLMUSDC'):
		pair_listings.append(symbol)

	if SYMBOL_STR.__contains__('XLMTUSD'):
		pair_listings.append(symbol)
	if SYMBOL_STR.__contains__('XLMETH'):
		pair_listings.append(symbol)

	if SYMBOL_STR.__contains__('XLMBTC'):
		pair_listings.append(symbol)

	if SYMBOL_STR.__contains__('XLMBNB'):
		pair_listings.append(symbol)


for symbol in pair_listings:
	print(symbol)


#XLMBTC, XLMETH, XLMBNB, XLMUSDT, XLMPAX


#TUSD USDC USDT
	

#print(parsed_json)




