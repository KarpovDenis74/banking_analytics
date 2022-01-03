import os
from datetime import timedelta
from distutils.util import strtobool
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', '')
DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'False'))
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*']
SITE_ID = 1
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'django_filters',
    'corsheaders',
    'captcha',
    'django.contrib.sites',
    'sorl.thumbnail',
]
USER_APPS = [
    'apps.api',
    'apps.currency',
    'apps.banks',
    'apps.users',
    'apps.news',
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


if DEBUG:
    INSTALLED_APPS += ['debug_toolbar'] + USER_APPS
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    # подключаем модуль отправки писем по e-mail
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('DEBUG_EMAIL_HOST')
    EMAIL_PORT = os.getenv('DEBUG_EMAIL_PORT')
    EMAIL_HOST_USER = os.getenv('DEBUG_EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('DEBUG_EMAIL_HOST_PASSWORD')
    # EMAIL_USE_TLS
    EMAIL_USE_SSL = os.getenv('DEBUG_EMAIL_USE_SSL')
    # EMAIL_TIMEOUT
    # EMAIL_SSL_KEYFILE
    # EMAIL_SSL_CERTFILE

    # подключаем Redis
    REDIS_HOST = os.getenv('DEBUG_REDIS_HOST')
    REDIS_PORT = os.getenv('DEBUG_REDIS_PORT')


else:
    INSTALLED_APPS += USER_APPS
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
    # подключаем модуль отправки писем по e-mail
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    # EMAIL_USE_TLS
    EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
    # EMAIL_TIMEOUT
    # EMAIL_SSL_KEYFILE
    # EMAIL_SSL_CERTFILE

    # подключаем Redis
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')

ROOT_URLCONF = 'banking_analytics.urls'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'banking_analytics.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'W-SU'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 40,
}
SIMPLE_JWT = {
    'SLIDING_TOKEN_LIFETIME': timedelta(days=40),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=40),
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles'), )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = 'core:index'
LOGOUT_REDIRECT_URL = 'core:index'
AUTH_USER_MODEL = 'users.User'

SITE_NAME = 'analitik.online'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Celery Configuration Options
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCERT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
