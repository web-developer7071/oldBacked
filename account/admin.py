from django.contrib import admin
from .models import User, MobileNo
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.register(User)

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User And Admin Role',
            {
                'fields': (
                    'user_type',
                    'admin_user',
                    'admin_service_type',
                    'term_cond'
                )
            }           
        ),
        (
            'User Live Permissions',
            {
                'fields': (
                    'Today_Status',
                    'Current_Status',
                    'Collected_No',
                    'Running_No'
                )
            }
        )
    )
admin.site.register(User, CustomUserAdmin)

# admin.site.register(User, UserAdmin)
# UserAdmin.fieldsets += ("User Role",{'fields':('user_type',)}),


class MobileNoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Mobile_No', 'created', 'updated')
admin.site.register(MobileNo, MobileNoAdmin)


