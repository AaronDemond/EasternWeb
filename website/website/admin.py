
from django.contrib import admin
from .models import GC, EasternWebAccount

class EasternWebAccountAdmin(admin.ModelAdmin):
	pass


class GCAdmin(admin.ModelAdmin):
	pass

admin.site.register(GC, GCAdmin)
admin.site.register(EasternWebAccount, EasternWebAccountAdmin)
