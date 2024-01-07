from pathlib import Path
import sys
import environ
import os
from django.utils.translation import gettext_lazy as _

from datetime import timedelta

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# env.read_env('.env')
env.read_env(env_file=str(BASE_DIR) + '/.env')    


# SECURITY WARNING: keep the secret key used in production secret
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Application definition
INSTALLED_APPS = [
    'channels',
    
    # translation
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # redirect
    'django.contrib.redirects',

    # nondefault
    'app.apps.AppConfig',
    'django.contrib.postgres',

    # Third Party
    'storages',
    'django_hosts',
    
    # REST
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',

]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # Set the desired maximum memory size (in bytes)

LOGIN_URL='/login/'
LOGIN_REDIRECT_URL='/login/'


MIDDLEWARE = [
    
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.gzip.GZipMiddleware', # should these three come first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',  #language. order must be in this way.
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
    'corsheaders.middleware.CorsMiddleware', # prevent error due CORS rules

    'classes.middleware.Log500ErrorsMiddleware', # Inernal server error logging
]


# IF THESE ARE TURNED ON, SAFARI DOESN'T WORK
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

USE_I18N = True
USE_L10N = True

ROOT_URLCONF = 'classes.urls.urls'
ROOT_HOSTCONF = 'classes.hosts' 
DEFAULT_HOST = 'static'
PARENT_HOST = env('PARENT_HOST')

# For testing and debugging
INTERNAL_IPS = [
    "127.0.0.1",
]


# match with the admin site
SITE_ID = int(env('SITE_ID'))
LANGUAGE_CODE = 'en'
LOCALE_PATHS = [os.path.join(str(BASE_DIR), 'locale')]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.custom_context_processor.custom_list', #custom_list
            ],
        },
    },
]


WSGI_APPLICATION = 'classes.wsgi.application'
ASGI_APPLICATION = 'classes.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Custom Auth Backend for Email
AUTHENTICATION_BACKENDS = [
    'classes.backends.ExtendedUserModelBackend',
    ]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
USE_I18N = True
LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('ja', _('Japanese')),
]

TIME_ZONE = 'UTC'

USE_TZ = True


# Static & Media Storage
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# https://testdriven.io/blog/django-digitalocean-spaces/ 



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Fields
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

