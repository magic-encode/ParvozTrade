from .models import CustomUser

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = [ 'fullname','username', 'email', 'password1', 'password2']
        


class ChangeUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']



