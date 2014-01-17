from .base import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/coalio-messages'
DEFAULT_FROM_EMAIL = 'digitaltextbookstudy@gmail.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', '..', 'coalio.db'),
    }
}

WSGI_APPLICATION = 'coalio.wsgi.dev.application'

