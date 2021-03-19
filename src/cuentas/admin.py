from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cuentas.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    read_only_fields = ('date_joined', ' last_login')

    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
        }),
    )

admin.site.register(Account, AccountAdmin)