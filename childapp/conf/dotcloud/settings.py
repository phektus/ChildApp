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

MEDIA_ROOT = '/home/dotcloud/code/childapp/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
MEDIA_URL = '/static/'

EMAIL_HOST = env['DOTCLOUD_MAILER_SMTP_HOST']
EMAIL_PORT = env['DOTCLOUD_MAILER_SMTP_PORT']
EMAIL_HOST_USER = env['DOTCLOUD_MAILER_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = env['DOTCLOUD_MAILER_SMTP_PASSWORD']
DEFAULT_FROM_MAIL = 'phektus@gmail.com'
APP_URL = 'http://childapp-hqkpjekb.dotcloud.com/'
