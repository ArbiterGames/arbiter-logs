"""
Django settings for logs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import dj_database_url


PROJECT_ROOT = os.path.abspath(os.path.split(os.path.split(__file__)[0])[0])
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = '9h7d@@*1&^w3rj!s99(iwt44fm(*w6&-h(x^fso%$tu=l7+b$s'
DEBUG = True
TEMPLATE_DEBUG = True
IS_DEV = os.environ['ENVIRONMENT'] == 'dev'
IS_STAGING = os.environ['ENVIRONMENT'] == 'staging'
IS_PRODUCTION = os.environ['ENVIRONMENT'] == 'production'

if IS_DEV:
    URL_ORIGIN = 'http://localhost:5000'
    DATABASE_URL = 'postgres://postgres@localhost/arbiterlogs'

if IS_STAGING:
    DATABASE_URL = os.environ['DATABASE_URL']

if IS_PRODUCTION:
    DEBUG = False
    DATABASE_URL = os.environ['DATABASE_URL']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'logs.urls'
WSGI_APPLICATION = 'logs.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
