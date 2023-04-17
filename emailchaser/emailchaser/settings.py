"""
Django settings for emailchaser project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$ewbz1=_4k#p9du5l&%wjmw83_6c&abs_-f+y)67^de0$y+tz$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "oauth2_provider",
    "smtp_imap_provider",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.microsoft",
    "lead",
    "campaign"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "emailchaser.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "emailchaser.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

GOOGLE_OAUTH2_CLIENT_CONFIG = {
    "web": {
        "client_id": "1003448645050-gk8m8u7g0piv5qtlag7aidcd2rk451lg.apps.googleusercontent.com"
    }
}

GOOGLE_OAUTH2_SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]
GOOGLE_OAUTH2_CALLBACK_URL = "http://localhost:8080/"
GOOGLE_CLIENT_ID = (
    "1003448645050-gk8m8u7g0piv5qtlag7aidcd2rk451lg.apps.googleusercontent.com"
)
GOOGLE_CLIENT_SECRET = "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"
# django-allauth settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "SCOPE": ["email", "profile"],
            "AUTH_PARAMS": {"access_type": "online"},
            "METHOD": "oauth2",
            "client_id": GOOGLE_CLIENT_ID,
            "secret": GOOGLE_CLIENT_SECRET,
            # "redirect_uri": "http://127.0.0.1:8000/",
            "OAUTH_PKCE_ENABLED": True,
            "VERIFIED_EMAIL": False,
            "HIDDEN": False,
            "ORDER": 1,
        }
    },
    "microsoft": {
        "SCOPE": ["openid", "email", "profile"],
        # "tenant": secrets.AZURE_AD_TENANT_ID,
        # "client_id": secrets.AZURE_AD_CLIENT_ID,
    },
}


SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_STORE_TOKENS = True
# LOGIN_REDIRECT_URL = "/oauth2/google-thanks/"
ACCOUNT_ADAPTER = "oauth2_provider.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "oauth2_provider.adapters.SocialAccountAdapter"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
