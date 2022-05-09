from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.\

#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
os.path.join(BASE_DIR, 'boot'),

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$q4k#hhd&+^nww7+ev=_!*-xew9i+*z2^sh03233pjam8-xpmo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'crud',
    'crispy_forms',
    "django_pagination_bootstrap",
    'django.contrib.postgres',
    'bootstrap_datepicker_plus',
    "bootstrap4",
    'bootstrap_pagination',
    'djmoney',
    'djmoney.contrib.exchange',
    'celery',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'Project_Demo.default_language_middleware.DefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_pagination_bootstrap.middleware.PaginationMiddleware",

]

ROOT_URLCONF = 'Project_Demo.urls'

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.request"
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'Project_Demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_demo',
        'USER': 'postgres',
        'PASSWORD': '0308',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-US'

LANGUAGES = [
    ('en', _('English')),
    ('vi', _('Vietnamese')),
]

# DEFAULT_LANGUAGE = 1

LOCALE_PATHS = (os.path.join(os.path.dirname(__file__), "..", "locale"),)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static",]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATE_FORMAT = "d-m-y"

LANGUAGE_SESSION_KEY = 'session_language_crud'
LANGUAGE_COOKIE_NAME = 'cookie_language_crud'

CURRENCY_RATES_URL = 'https://api.currencyapi.com/v3/latest?apikey=1Rh0P0R6bqhq6AulfXL9gwCBpFyEuAHXqmdcaNn1'

BASE_CURRENCY = "USD"

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        'TIMEOUT': 86400,
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://localhost:6379/0")

CELERY_BEAT_SCHEDULE = {
    'update_rates': {
    'task': 'update_rates',
    'schedule': 5.0,
    }
}

CURRENCIES = ('USD', 'VND')
