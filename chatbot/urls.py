# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/chatbot', views.chatbot_api_view, name='chatbot_api'),  # Define URL pattern for chatbot API endpoint
    # Add other URL patterns as needed
]
