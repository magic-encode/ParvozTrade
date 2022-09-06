from django import forms

from .models import CustomUser
from .models import CommentsBlog

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



class CommentsBlogForm(forms.ModelForm):
    class Meta:
        model = CommentsBlog
        fields = ('body', )
        
    def __init__(self, *args, **kwargs):
        super(CommentsBlogForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

