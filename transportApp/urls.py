from django.urls import path
from transportApp import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.user_details , name='user-details'),
    path('change-password', views.change_password, name='change-password'),
    path('login/',auth_views.LoginView.as_view(template_name ='login.html'), name = 'login'),
]