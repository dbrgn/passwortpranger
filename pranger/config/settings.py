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

DEBUG = env('DJANGO_DEBUG', 'False').lower() in true_values
TEMPLATE_DEBUG = DEBUG
SHOW_DEBUG_TOOLBAR = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': dj_database_url.config(),
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['pranger.herokuapp.com', 'passwortpranger.ch', 'www.passwortpranger.ch']

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

# Make this unique, and don't share it with anybody.
SECRET_KEY = env('SECRET_KEY', 'DEBUG_SECRET_KEY')
if SECRET_KEY == 'DEBUG_SECRET_KEY' and DEBUG is False:
    raise ImproperlyConfigured('Missing SECRET_KEY env variable. You can ' +
            'generate one with `./manage.py generate_secret_key`.')

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
)

INSTALLED_APPS = (
    # Builtin apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # 3rd party apps
    'messagegroups',
    'crispy_forms',
    'compressor',
    'storages',

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
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
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

# Static files
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
STATIC_ROOT = PROJECT_ROOT.child('static')
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = not DEBUG
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
    'compressor.filters.template.TemplateFilter',
)
COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'pyscss {infile} -o {outfile}'),
)
COMPRESS_PARSER = 'compressor.parser.LxmlParser'
if DEBUG:
    MEDIA_ROOT = PROJECT_ROOT.child('media')
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
else:
    AWS_STORAGE_BUCKET_NAME = 'passwortpranger'
    AWS_PRELOAD_METADATA = True
    AWS_QUERYSTRING_AUTH = False  # Don't include auth in every url
    AWS_ACCESS_KEY_ID = require_env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = require_env('AWS_SECRET_ACCESS_KEY')
    STATIC_URL = 'https://{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
    MEDIA_URL = 'https://{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'config.storage.CachedS3BotoStorage'
    COMPRESS_STORAGE = STATICFILES_STORAGE
    THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Templates
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# Debug toolbar
def show_debug_toolbar(request):
    return DEBUG
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'config.settings.show_debug_toolbar',
}
DEBUG_TOOLBAR_PATCH_SETTINGS = False
