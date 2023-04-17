from django.urls import path
from .views import google_after_login_callback, outlook_oauth2_callback

urlpatterns = [
    # path('google-thanks/', google_after_login_callback, name='google_callback'),
    # path('outlook/callback/', outlook_oauth2_callback, name='outlook_callback'),
]
