"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ot+m-ipagytcw9foa7qf=io7cq!p_98-+l(z%y9e*rqb#6&r%%'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1', 
# 'http://capstone-dev-clone.us-west-2.elasticbeanstalk.com', 
# 'http://ec2-52-38-115-174.us-west-2.compute.amazonaws.com']



# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'app',
	'rest_framework',
	'rest_framework.authtoken',
]

# from app.permissions import CsrfExemptSessionAuthentication


REST_FRAMEWORK = {
	# 'DEFAULT_PERMISSION_CLASSES': (
	# 	# 'rest_framework.permissions.IsAuthenticated',
	# 	'rest_framework.permissions.AllowAny',
	# ),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		# 'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.TokenAuthentication',
	)
}

MIDDLEWARE_CLASSES = [ 
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
			],
		},
	},
]

WSGI_APPLICATION = 'project.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# 	},
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DEBUG = True
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql', 
		'NAME': 'capstone', 
		'USER': 'root', 
		'PASSWORD': 'reapak', 
		'HOST': 'localhost', 
		'PORT': '',
	}
}

try:
	from local_settings import *
except ImportError:
	pass










