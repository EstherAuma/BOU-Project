
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import PasswordChangeCustomForm
from django.core.mail import send_mail
from django.conf import settings
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

def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']

        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently= False
        )

    return render(request,'index.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            
            send_mail(
                'Password Change',
                f'Hello {request.user.username}, your password has been changed successfully. Please keep it secure and do not share it with anyone.\n\n'
                f'Please note that you won\'t be allowed to log in with the old password that has already been changed.',

                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False
            )
        
            return redirect('login') 
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'change-password.html', {'form': form})
