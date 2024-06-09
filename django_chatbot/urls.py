# my_project/urls.py

from django.contrib import admin
from django.urls import path, include           # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),         # Include frontend app URLs
    path('chatbot/', include('chatbot.urls')),   # Include chatbot app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Django built-in auth views
]
