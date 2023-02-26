from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BaseUser
from .models import NGOModel
from .models import VolunteerModel

class UserAdminConfig(UserAdmin):
    model = BaseUser

    search_fields = ("username", "email")
    list_filter = ("username", "email", "is_active", "is_superuser")

    ordering = ("-create_date",)

    list_display = ("email","role" ,"is_active", "is_staff")

    readonly_fields = ("create_date",)

    fieldsets = (
        (None, {"fields" : ("email", "role")}),
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
                    "role",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(BaseUser, UserAdminConfig)

admin.site.register(NGOModel)
admin.site.register(VolunteerModel)