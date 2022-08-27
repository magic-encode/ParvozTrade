from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUserForm
from .forms import ChangeUserForm

from .models import  Post
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = ChangeUserForm
    model = CustomUser
    
    list_display = ['fullname','username', 'email', 'is_staff', 'number']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fullname', 'number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('fullname', 'number')}),
    )


admin.site.register(Post)
admin.site.register(CustomUser, CustomUserAdmin)