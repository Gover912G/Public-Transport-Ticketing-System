from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin  


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'is_passenger',
                    'is_conductor',
                    'is_Owner'
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
