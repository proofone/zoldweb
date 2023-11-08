from django.contrib import admin
from entities.models import User, Community, Location, OtherEntity


class UserAdmin(admin.ModelAdmin):
    exclude =  []


class CommunityAdmin(admin.ModelAdmin):
    exclude =  []


class LocationAdmin(admin.ModelAdmin):
    exclude =  []


class OtherEntityAdmin(admin.ModelAdmin):
    exclude =  []


admin.site.register(User, UserAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(OtherEntity, OtherEntityAdmin)
admin.site.register(Location, LocationAdmin)
