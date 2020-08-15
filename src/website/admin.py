from django.contrib import admin

from .models import Signal, Trade, HistoricalPrice, HistoricalTrend, Candle


class HPA(admin.ModelAdmin):
	pass

class HTA(admin.ModelAdmin):
	pass

class CandleAdmin(admin.ModelAdmin):
	pass

class SignalAdmin(admin.ModelAdmin):
	pass

class GCAdmin(admin.ModelAdmin):
	pass

class TradeAdmin(admin.ModelAdmin):
	pass

class APAdmin(admin.ModelAdmin):
	pass

# model must be registered 
# to appear on admin page
admin.site.register(HistoricalPrice, HPA)
admin.site.register(Candle, CandleAdmin)
admin.site.register(HistoricalTrend, HTA)
admin.site.register(Signal, SignalAdmin)
admin.site.register(Trade, TradeAdmin)

