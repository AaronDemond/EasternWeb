
from django.contrib import admin
from .models import GC, EasternWebAccount, Asset

class EasternWebAccountAdmin(admin.ModelAdmin):
	pass

class AssetAdmin(admin.ModelAdmin):
	pass

#class CustomAdminSite(AdminSite)
#	site_header = 'Custom Admin Site'
#
#	def
#

class GCAdmin(admin.ModelAdmin):
	pass

admin.site.register(GC, GCAdmin)
admin.site.register(EasternWebAccount, EasternWebAccountAdmin)
admin.site.register(Asset, AssetAdmin)
