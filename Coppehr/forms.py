from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label_suffix='',
        widget=forms.TextInput(attrs={'class': 'form-control border-dark'}))

    password = forms.CharField(
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control border-dark'}))