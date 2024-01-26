from django.urls import path
from transportApp import views

urlpatterns = [
    path('', views.change_password , name='change-password'),
    path('change-password2', views.new , name='change-password2'),

]