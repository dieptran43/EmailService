"""
Django settings for emailservice project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
'api',
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#r5dd*##m-z*gjew$n!=fo#^*)lp1^-d*1ufx&_3d9-wq5v8vr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
MANDRILL_API_KEY="XXX"

EMAIL_BACKEND="djrill.mail.backends.djrill.DjrillBackend"

# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin.apps.SimpleAdminConfig',
    ## 3rd party
    'rest_framework',
    'rest_framework_swagger',
    'djrill',
    ## custom
    'tokenauth',
    'api',

    # testing etc:
    'django_jenkins',
    'django_extensions',
    'corsheaders',
)

# CUSTOM AUTH
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'tokenauth.authbackends.TokenAuthBackend'
)

## REST
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'tokenauth.authbackends.RESTTokenAuthBackend',
    ),
    'DEAFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    ## add this:
    'tokenauth.middleware.TokenAuthMiddleware',
)

ROOT_URLCONF = 'emailservice.urls'

WSGI_APPLICATION = 'emailservice.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Services:

## Service base urls without a trailing slash:
USER_SERVICE_BASE_URL = 'http://staging.userservice.tangentme.com'

PROJECT_APPS = (
    'api',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    # 'django_jenkins.tasks.run_sloccount',
    # 'django_jenkins.tasks.run_graphmodels'
)

SWAGGER_SETTINGS = {
    'api_key': '8600754f305f0c00ce42e9a53cc42dbe0b89650f',
    'info': {
    'contact': 'admin@tangentsolutions.co.za',
    'description': 'A microservice for handling project status and information. From scaffolding 3rd party tools etc to managing resourcing and project tracking',
    'license': 'MIT',
    'title': 'EmailService',
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/srv/www/emailservice/static/'

