from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    lastname=forms.CharField()
    password = forms.CharField()
    email = forms.CharField()

