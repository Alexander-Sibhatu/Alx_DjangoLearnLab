from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

admin .site.register(Book)

class BookAdmin(admin.ModelAdmin):

    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional Info",
            {
                "fields": (
                    "date_of_birth",
                    "profile_photo"
                )
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)