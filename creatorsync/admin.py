from django.contrib import admin
from .models import CreatorProfile, Campaign, Application, Shipment


admin.site.register(CreatorProfile)
admin.site.register(Campaign)
admin.site.register(Application)
admin.site.register(Shipment)