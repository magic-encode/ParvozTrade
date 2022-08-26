from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Post
from .forms import UserChangeForm
from .forms import UserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser


admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(CustomUserAdmin)