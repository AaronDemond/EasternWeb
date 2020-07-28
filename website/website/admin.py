
from django.contrib import admin
from .models import  Asset,  Trade, Signal, HistoricalTrend, HistoricalPrice



class HistoricalPriceAdmin(admin.ModelAdmin):
	pass

class HistoricalTrendAdmin(admin.ModelAdmin):
	pass


class SignalAdmin(admin.ModelAdmin):
	pass

class AssetAdmin(admin.ModelAdmin):
	pass


class GCAdmin(admin.ModelAdmin):
	pass

class TradeAdmin(admin.ModelAdmin):
	pass

class APAdmin(admin.ModelAdmin):
	pass

admin.site.register(HistoricalPrice, HistoricalPriceAdmin)
admin.site.register(HistoricalTrend, HistoricalTrendAdmin)
admin.site.register(Signal, SignalAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(Asset, AssetAdmin)
