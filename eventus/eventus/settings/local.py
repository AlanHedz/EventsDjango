from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eventusdb',
        'USER': 'root',
        'PASSWORD': 'lol123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')