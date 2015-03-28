"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i$x!6%1f32s3!c@pt=556wv=i44sc#8z_!7n-g5#br%gou86)6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'accounts',
    'shop',
    'catalog',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ajaxuploader',
    'redactor',
    'banners',
    'pages',
)
# Application definition


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'daryashop_db',
        'USER': 'daryashop',
        'PASSWORD': 'zaqxswcde',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


REDACTOR_OPTIONS = {'lang': 'ru'}
REDACTOR_UPLOAD = 'static'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR,  'catalog/templates'),
    os.path.join(BASE_DIR,  'pages/templates'),
    os.path.join(BASE_DIR,  'shop/templates'),
)

UIT_CONFIG = {
    'MENU': (

        # Keep original label and models
        'sites',

        # Rename app and set icon
        {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},

        # Reorder app models
        {'app': 'auth', 'models': ('user', 'group')},

        # Custom app, with models
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},

        # Cross-linked models with custom name; Hide default icon
        {'label': 'Custom', 'icon':None, 'models': (
            'auth.group',
            {'model': 'auth.user', 'label': 'Staff'}
        )},

        # Custom app, no models (child links)
        {'label': 'Users', 'url': 'auth.user', 'icon':'icon-user'},

        # Separator
        '-',

        # Custom app and model with permissions
        {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
            {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
        ]},
    )
}

AUTH_USER_MODEL = 'accounts.User'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'marshinskii@gmail.com'
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'marshinskii@gmail.com'
EMAIL_HOST_PASSWORD = 'Avagon_VIP'
EMAIL_PORT = 587

