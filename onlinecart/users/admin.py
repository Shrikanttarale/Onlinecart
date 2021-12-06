from django.contrib import admin

from .forms import CustomUserForm
from .models import CustomUsers
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model=CustomUsers
    add_form = CustomUserForm
    fieldsets = (*UserAdmin.fieldsets,
                 (
                 'User Photo',
                 {
                     'fields':('user_photo',)
                 })
                 )

admin.site.register(CustomUsers,CustomUserAdmin)