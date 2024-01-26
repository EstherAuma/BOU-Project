from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import StaffUser


class CustomProfileChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = StaffUser
        fields = ('first_name', 'last_name', 'email', 'department', 'phone_number')

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = StaffUser