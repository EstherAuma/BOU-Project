from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import CustomProfileChangeForm, CustomPasswordChangeForm

# Create your views here.
def change_password(request):
    try:
        solo_user = StaffUser.objects.get(username='solo')
    except StaffUser.DoesNotExist:
        # Handle the case where the user with username 'solo' does not exist
        solo_user = None

    context = {
        'solo_user': solo_user,
    }
    
    return render(request, 'change-password.html', context)

def new(request):
    return render(request, 'change-password2.html')