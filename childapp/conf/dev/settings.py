from childapp.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'childapp.conf.dev.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'childapp',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
