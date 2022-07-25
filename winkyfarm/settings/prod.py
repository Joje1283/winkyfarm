from .common import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]
ALLOWED_HOSTS += [os.getenv("ALLOWED_HOST")]
CSRF_TRUSTED_ORIGINS = ["https://*.joje.link"]  # 안전하지 않은 요청에 대한 신뢰할 수 있는 출처 목록 (CSRF 오류로 인해 설정)
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

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)