from django.contrib import admin

from apps.users.models import (CommunicationNetwork, User,
                               UserCommunicationNetwork)


class MembershipInline(admin.TabularInline):
    model = UserCommunicationNetwork
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [MembershipInline, ]
    list_display = ("pk", "username", "first_name", "last_name", "email",
                    "is_staff", "is_active", "date_joined")
    search_fields = ("username", )
    list_filter = ("email",)
    empty_value_display = "-пусто-"


class CommunicationNetworkAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "site")
    search_fields = ("name", )
    list_filter = ("site",)
    empty_value_display = "-пусто-"


admin.site.register(User, UserAdmin)
admin.site.register(CommunicationNetwork, CommunicationNetworkAdmin)
