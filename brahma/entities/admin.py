from django.contrib import admin
from entities.models import User, Community, Location, OtherEntity, CommunityMembership


class CommunityMembershipInline(admin.TabularInline):
    model = Community.members.through


class UserAdmin(admin.ModelAdmin):
    exclude =  []


class CommunityAdmin(admin.ModelAdmin):
    exclude =  []
    inlines = [CommunityMembershipInline]


class LocationAdmin(admin.ModelAdmin):
    exclude =  []


class OtherEntityAdmin(admin.ModelAdmin):
    exclude =  []


admin.site.register(User, UserAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(OtherEntity, OtherEntityAdmin)
admin.site.register(Location, LocationAdmin)
