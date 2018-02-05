from django import forms

from blog.models import *

class PersonForm(forms.ModelForm):
    account = forms.CharField(label='帐号', required=True)
    passwd = forms.CharField(label='密码', widget=forms.PasswordInput(),required=True)
    class Meta:
        model = Person
        fields = ('account', 'passwd')


