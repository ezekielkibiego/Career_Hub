from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class SuperApplicantAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "user_type",
        "is_superuser",
        "is_staff",
        "is_admin",
        "first_name",
        "last_name",
        "last_login",
        "date_joined",
        "is_active",
    )

    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )


admin.site.register(CustomUser, SuperApplicantAdmin)
admin.site.register(Applicant, SuperApplicantAdmin)
admin.site.register(ApplicantProfile)


class SuperEmployerAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "date_joined",
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "is_admin",
    )

    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )


# admin.site.register(CustomUser, SuperEmployerAdmin)
admin.site.register(Employer, SuperEmployerAdmin)
admin.site.register(EmployerProfile)
