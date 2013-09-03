# -*- coding: utf-8 -*-
# Django settings for pranger project.
from __future__ import print_function, division, absolute_import, unicode_literals

import os

from django.core.exceptions import ImproperlyConfigured

import dj_database_url
from unipath import Path


# Helper functions

def env(name, default=None):
    return os.environ.get(name, default)

def require_env(name):
    value = env(name)
    if not value:
        raise ImproperlyConfigured('Missing {} env variable'.format(name))
    return value

true_values = ['1', 'true', 'y', 'yes', 1, True]


# Main configuration

DEBUG = require_env('DJANGO_DEBUG')
TEMPLATE_DEBUG = DEBUG
SHOW_DEBUG_TOOLBAR = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(),
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Internal IPs
INTERNAL_IPS = ('127.0.0.1',)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Path to the project root
PROJECT_ROOT = Path(__file__).ancestor(2)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT.child('static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env('SECRET_KEY', 'DEBUG_SECRET_KEY')
if SECRET_KEY == 'DEBUG_SECRET_KEY' and DEBUG is False:
    raise ImproperlyConfigured('Missing SECRET_KEY env variable. You can ' +
            'generate one with `./manage.py generate_secret_key`.')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
     'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
)

INSTALLED_APPS = (
    # Builtin apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # 3rd party apps
    'south',
    'social_auth',
    'messagegroups',

    # Own apps
    'front',
)

if DEBUG:
    INSTALLED_APPS += (
        'django_extensions',
        'debug_toolbar',
    )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Email configuration
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Auth
AUTH_USER_MODEL = 'front.User'
AUTHENTICATION_BACKENDS = ('social_auth.backends.google.GoogleOAuth2Backend',)
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/auth/login-successful/'
LOGIN_ERROR_URL = '/auth/login-error/'
GOOGLE_OAUTH2_CLIENT_ID = require_env('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = require_env('GOOGLE_OAUTH2_CLIENT_SECRET')
#GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {'access_type': 'offline'}
GOOGLE_OAUTH_EXTRA_SCOPE = [
    # Add extra scopes here, e.g.
    # 'https://www.googleapis.com/auth/userinfo.profile',
    # 'https://adwords.google.com/api/adwords',
]
#GOOGLE_WHITE_LISTED_DOMAINS = []
SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL
SOCIAL_AUTH_DEFAULT_USERNAME = 'socialauth_user'
SOCIAL_AUTH_UUID_LENGTH = 8
SOCIAL_AUTH_SLUGIFY_USERNAMES = True
SOCIAL_AUTH_URLOPEN_TIMEOUT = 15

# Testing
SOUTH_TESTS_MIGRATE = False

# Debug toolbar
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda request: SHOW_DEBUG_TOOLBAR
}
