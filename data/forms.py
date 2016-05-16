from django import forms
from .models import User

class NameFormField(forms.Form):
    name = forms.CharField(label='Nombre')

class UserForm(forms.ModelForm):

    name = forms.CharField(
                           widget = forms.TextInput(attrs={'id':'name', 'class':'active validate','placeholder':'Nombre Completo'})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Email','type':'email'})
    )
    birth_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'type': 'date'})
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Password','type':'password'})
    )

    class Meta:
        model = User
        fields = '__all__'
        '''fields_classes = {
            'name' : NameFormField,
        }'''