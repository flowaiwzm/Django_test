# from django.conf.urls import url
# from django.contrib.auth.views import login
from django.urls import path,include 
from . import views

app_name='users'
urlpatterns = [
    # Login page.
    path('',include("django.contrib.auth.urls")),
        
    
    # Registration page. 
    path('register/', views.register, name='register'),
]