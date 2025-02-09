"""
Django settings for SummerSchool project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('DJANGO_DEBUG', 'True') == 'True':
    DEBUG = True
    print('Django running in debug mode!')
else:
    DEBUG = False

# django email for registration
DEFAULT_FROM_EMAIL = '18810307602@139.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.139.com'
EMAIL_HOST_USER = '18810307602'
EMAIL_HOST_PASSWORD = 'xxliZGYD2019'

# official email for important notification
OFFICIAL_EMAIL_HOST = 'mails.tsinghua.edu.cn'
OFFICIAL_FROM_EMAIL = 'li-xx15@mails.tsinghua.edu.cn'
OFFICIAL_EMAIL_HOST_USER = 'li-xx15@mails.tsinghua.edu.cn'
OFFICIAL_EMAIL_HOST_PASSWORD = 'lixx2015'

# registration
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = 'profile'
DEADLINE = {'year': 2019, 'month': 3, 'day': 13, 'hour': 12}

# website
WEBSITE = os.getenv('DJANGO_WEBSITE', 'www1.ep.tsinghua.edu.cn:8000')
YEAR = int(os.getenv('DJANGO_YEAR', '2019'))

# for deployment
if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    ALLOWED_HOSTS = ['*', ]
    X_FRAME_OPTIONS = 'DENY'
else:
    ALLOWED_HOSTS = ['*', ]

FILE_UPLOAD_PERMISSIONS = 0o644

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yp=gxh$en^(hkwn@!m59$9%f5ja#mt&nsa&3k$m&fb)!(jjy$d'

# Application definition

INSTALLED_APPS = [
    'student_info',
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'graduate_admission.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'student_info.context_processors.global_settings',
            ],
            'builtins': [
                'student_info.filters'
            ],
        },
    },
]

WSGI_APPLICATION = 'graduate_admission.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'graduate_admission_%s.sqlite3' % YEAR),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
