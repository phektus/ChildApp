from childapp.conf.settings import *
import json

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'childapp.conf.dotcloud.urls'

with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'childapp',
    'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
    'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
    'HOST': env['DOTCLOUD_DB_SQL_HOST'],
    'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
  }
}

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)

# edit settings.py file to the following.
ADMIN_MEDIA_PREFIX = '/static/admin/'
# change MEDIA_URL
MEDIA_URL = '/static/'

# for smtp
EMAIL_HOST = 'childapp-HQKPJEKB.dotcloud.com'
EMAIL_PORT = 31618
EMAIL_HOST_USER = 'dotcloud'
EMAIL_HOST_PASSWORD = 'nQtBEurWBWBZ0GvPVdco'
DEFAULT_FROM_MAIL = 'phektus@gmail.com'
APP_URL = 'http://childapp-hqkpjekb.dotcloud.com/'
