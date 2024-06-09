# frontend/urls.py

from django.urls import path
from .views import base, chat, signin, signup 

urlpatterns = [
    path('', base, name='base'),
    path('chat/', chat, name='chat'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    
]
