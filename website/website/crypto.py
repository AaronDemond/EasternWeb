from website.models import Signal
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
		
	

