
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import PasswordChangeCustomForm
from django.core.mail import send_mail

from django.contrib import messages

# Create your views here.
def user_details(request):
    try:
        essie_user = StaffUser.objects.get(username='essie')
    except StaffUser.DoesNotExist:
        # Handle the case where the user with username 'essie' does not exist
        essie_user = None

    context = {
        'essie_user': essie_user,
    }

    return render(request, 'user-details.html', context)


@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 

            subject = 'Change password'

            message = 'Hey you have successfully changed your password'
            to = user.email
            send_mail(
                subject,
                message,
                'estheraumaego@gmail.com',
                [to],
                fail_silently=False
            )
            return redirect('login')  
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'change-password.html', {'form': form})
    
    
