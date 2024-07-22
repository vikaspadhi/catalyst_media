from allauth.account.forms import LoginForm 
from django import forms
from django.contrib.auth.models import User

class CustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)
    

class AdminAddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = User
        fields = ['username','email']

    def save(self, commit=True):
        user = super(AdminAddUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user