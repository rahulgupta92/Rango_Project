"""
Django settings for classifiedsystem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR=os.path.dirname(__file__)

PROJECT_PATH=os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH=os.path.abspath(PROJECT_PATH)

TEMPLATE_PATH=os.path.join(PROJECT_PATH,'templates')

STATIC_PATH=os.path.join(PROJECT_PATH,'static')

DATABASE_PATH=os.path.join(PROJECT_PATH,'classifieds.db')

TEMPLATE_DIRS=(
    #'/home/ht/projects/classifiedsystem/templates',

    TEMPLATE_PATH,
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0#v_nxv8ma#l%xpj!em^cz(qktmhcrhrl^h3slrk3mxjp+urpc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'classifieds',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'classifiedsystem.urls'

WSGI_APPLICATION = 'classifiedsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }

}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



STATIC_URL = '/static/'

STATICFILES_DIRS=(
   # '/home/ht/projects/classifiedsystem/static',
   STATIC_PATH,
)




#STATIC_PATH=os.path.join(/home/ht/projects/classifiedsystem,'static')

#STATIC_URL='/static/'

#STATICFILES_DIRS=(
   # STATIC_PATH,
    #)




MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(PROJECT_PATH,'media')
    #'/home/ht/projects/classifiedsystem/media'   #don't put comma here like above.it will look like we're passing tuple rather than string
   
    