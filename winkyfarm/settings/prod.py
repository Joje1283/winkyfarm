from .common import *

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]
ALLOWED_HOSTS += [os.getenv("ALLOWED_HOST")]

STATIC_ROOT = "/var/www/staticfiles/winkyfarm"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
if 'test' in sys.argv:
    DATABASES = {
        "default":
            {'ENGINE': 'django.db.backends.sqlite3'}
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'winkyfarm',
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
        }
    }