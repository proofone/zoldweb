from django.contrib import admin
from events.models import EventSession


class EventAdmin(admin.ModelAdmin):
    exclude =  []


admin.site.register(EventSession, EventAdmin)
