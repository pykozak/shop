import json
import os
import sys

from django.core.exceptions import ImproperlyConfigured

import mongoengine

SRC_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(SRC_DIR)

SECRET_FILE = os.path.join(ROOT_DIR, 'secrets.json')

with open(SECRET_FILE) as f:
    SECRETS = json.load(f)


def get_secret(setting, secrets=SECRETS):
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured('Set secret value: {0}'.format(setting))


SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'products',
    'basket',
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

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

SESSION_ENGINE = 'mongoengine.django.sessions'

SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

if 'test' not in sys.argv:
    MONGO = get_secret('MONGO')
    mongoengine.connect(**MONGO)
