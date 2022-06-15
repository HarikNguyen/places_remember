from django.contrib import admin
from .models import UserWithAvatar

@admin.register(UserWithAvatar)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ('user', 'avatar')