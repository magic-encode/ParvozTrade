from django.forms import ModelForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = [ 'first_name','username', 'email', 'password1', 'password2']
        

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        for field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ChangeUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email' ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})





