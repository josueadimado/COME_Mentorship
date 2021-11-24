from django.contrib import admin
from .models import CustomUser
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.conf import settings


class CustomUserAdmin(UserAdmin):
    model = CustomUser

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
