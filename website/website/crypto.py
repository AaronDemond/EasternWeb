
class Helper():
	def sort(self,signals):
		'''Accepts a queryset or list of signals and returns a
		   list sorted by its quantity
		'''
	
		list_object = []
		for s in signals:
			try:
				if s.qty and s.symbol==signals[0].symbol:
					list_object.append(s)
			except:
				pass
		def getQty(x):
			try:
				q=float(x.qty)

			except:
				q=0
			return q

		list_object.sort(key=getQty,reverse=True)
		return list_object


	def getSignalList(self,symbol='BTCUSDT'):
		'''returns a list object of the given symbol'''
		l=[]
		for s in Signal.objects.all().order_by("-id"):
			if s.symbol==symbol:
				l.append(s)
		return(l)

	def getBTCSignal(self):
		return("ETH SIGNAL")

	def getBTCSignal(self):
		return("ETH SIGNAL")


class DataAnalayzer():

	def __init__(self,data):
		self.data=data

	def __str__(self):
		return("data analyzer object")

	def getBigVolumeTradeList(self,alert_type,data,__symbol):
		bigVolumeTradeList=[]
		if alert_type == 'volume':
			for trade in data:
				if trade.qty>1:
					bigVolumeTradeList.append(trade)

		return bigVolumeTradeList

class SignalHelper():
	def getPriceChangeAlert(self,recentBTCUSDTPrice_QS, symbol_str):
			from website.models import Signal
			rbpq = recentBTCUSDTPrice_QS

			n = [float(rbpq[0].price), float(rbpq[1].price)]
				# n[0] = newer
			p_change = (((n[0] - n[1])/n[1]) * 100)
			if (p_change > 1):
				newSignal = Signal(symbol=symbol_str+" PRICE ALERT")
				s=newSignal.save()
				alert_str= "Price increase alert: " + symbol_str + " " + str(p_change)
				alert_str= alert_str + "\nFrom " + str(n[1]) + " to " + str(n[0])
			if (p_change < 0):
				newSignal = Signal(symbol=symbol_str+" PRICE ALERT")
				s=newSignal.save()
				alert_str= "Price decrease alert: " + symbol_str + " " + str(p_change)
				alert_str= alert_str + "\nFrom " + str(n[1]) + " to " + str(n[0])
			else:
				alert_str = "No major movement: " + symbol_str + " " + str(n[0])
				alert_str= alert_str + "\nFrom " + str(n[1]) + " to " + str(n[0])
			return alert_str

	def someFunction(self):
		return("hello world")

	def getBigTrades(self,symbol, tradelist, qty_min):
		bt=[]
		for trade in tradelist:
			if float(trade.qty) > qty_min:
				if trade.symbol == symbol:
					bt.append(trade)
		return bt

	
	
