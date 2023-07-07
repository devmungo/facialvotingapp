import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-olc_l4v9uimldmd)xjf0qcgbl#f3zyln(b##@b26_&2q_oo@_d'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

#ALLOWED_HOSTS = ['mywebsite.com', 'www.mywebsite.com', 'localhost', '127.0.0.1', '*']

# ALLOWED_HOSTS = ['*']

# CSRF_TRUSTED_ORIGINS = ['your-domain']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store', # Django app

    'account', # Django app

    'mathfilters',

    'crispy_forms', # Crispy forms


]

# Crispy forms

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [ 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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
                'store.views.categories',

            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#Default DB

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'static/media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Admin styling adjustment

#ADMIN_MEDIA_PREFIX = '/static/admin/'


# RDS (Database) configuration settings:


# AWS credentials:
'''
AWS_ACCESS_KEY_ID = "" # Access Key ID 
AWS_SECRET_ACCESS_KEY = "" # Secret Access Key ID

# S3 configuration settings:

AWS_STORAGE_BUCKET_NAME = '' 

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = False
'''


# Admin styling adjustment

#ADMIN_MEDIA_PREFIX = '/static/admin/'


# RDS (Database) configuration settings:

'''
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': '',

        'USER': '',

        'PASSWORD': '',

        'HOST': '',

        'PORT': '5432',


    }

}
'''




# AUTH_USER_MODEL = 'account.CustomUser'

# # # Email Configuration
# EMAIL_BACKEND = 'django_ses.SESBackend'
# AWS_ACCESS_KEY_ID = 'your-access-id'
# AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
# AWS_SES_REGION_NAME = 'your-region'
# AWS_SES_REGION_ENDPOINT = 'email.your-region.amazonaws.com'
# DEFAULT_FROM_EMAIL = 'your-email'
