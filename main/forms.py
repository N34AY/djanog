from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    username.widget.attrs.update({
        'class': 'form-control',
        'required': 'required',
        'id': 'login',
        'placeholder': 'login',
        'type': 'text'
    })
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs.update({
        'class': 'form-control',
        'required': 'required',
        'id': 'password',
        'placeholder': 'password',
        'type': 'password'
    })
