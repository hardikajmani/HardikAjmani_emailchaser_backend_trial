from django.urls import path
from .views import google_oauth2_callback, outlook_oauth2_callback

urlpatterns = [
    path('google-callback/', google_oauth2_callback, name='google_callback'),
    # path('outlook/callback/', outlook_oauth2_callback, name='outlook_callback'),
]
