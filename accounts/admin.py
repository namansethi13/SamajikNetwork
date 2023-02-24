from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BaseUser
from .models import NGO
from .models import Volunteer


class UserAdminConfig(UserAdmin):
    model = BaseUser

    search_fields = ("username", "email")
    list_filter = ("username", "email", "is_active", "is_superuser")

    ordering = ("-create_date",)

    list_display = ("email","is_active", "is_staff")

    readonly_fields = ("create_date",)

    fieldsets = (
        (None, {"fields" : ["email"]}),
        ("Verifications", {"fields" : ("is_email_verified",)}),
        ("Permisssions", {"fields" : ("is_active","is_staff", "is_superuser", "groups",)}),   
    )

    add_fieldsets = (
        (None, 
            {
                "classes" : ("wide", ), 
                "fields" : (
                    # "username",
                    "email", 
                    "password1",
                    "password2", 
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )

admin.site.register(BaseUser, UserAdminConfig)

admin.site.register(NGO)
admin.site.register(Volunteer)