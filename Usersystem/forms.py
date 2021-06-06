from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields


class signUP (UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={"class": "fadeIn second", "placeholder": "Email"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(signUP, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'fadeIn second'
        self.fields['username'].widget.attrs['placeholder'] = 'First Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'fadeIn third'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'fadeIn third'
        self.fields['password2'].widget.attrs['placeholder'] = 'ReEnter Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<div class="form-text text-muted"><small>Enter the same password as before, for verification</small></div>'




class Edit (UserChangeForm):
    password = forms.CharField( widget=forms.TextInput(attrs={"type": "hidden"}))
    class Meta:
        model = User
        fields = ("username","first_name","email","password")