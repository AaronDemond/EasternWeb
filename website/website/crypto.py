class Helper():
	def sort(self,signals):
		'''Accepts a queryset returns a 
		   list of sorted btc buy signals 
		'''
	
		list_object = []
		for s in signals:
			try:
				if s.qty and s.symbol=="BTCUSDT":
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

