class Helper():
	def print_methods(someObject):
		for something in dir(someObject):
			print(something)

	def print_big_trades(x, t):
		for trade in t[:10000]:
			if (trade.qty > 1):
				print(trade.price)
