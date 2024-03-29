from django import forms
from .models import StaffUser
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import CharField, PasswordInput,TextInput,EmailField, PasswordInput


class PasswordChangeCustomForm(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect': "The old password is incorrect. Please try again"}
    
    old_password = CharField(
        required=True,
        label='Old password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'The password cannot be empty'}
    )

    new_password1 = CharField(
        required=True,
        label='New password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'The password cannot be empty'}
    )

    new_password2 = CharField(
        required=True,
        label='Confirm new password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'The password cannot be empty'}
    )

    email = EmailField(
        required=True,
        label='Email',
        widget=TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'The email cannot be empty'}
    )

    