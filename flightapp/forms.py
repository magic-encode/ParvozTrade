from django import forms
from flightapp.models.sendmessage import GetInfo


class GetInfoForm(forms.ModelForm):

    class Meta:
        model = GetInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GetInfoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})