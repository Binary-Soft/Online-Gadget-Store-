"""
Django settings for Online_Gadget_Store project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = Path.joinpath(BASE_DIR, 'templates')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2=bd37ernpif+v@3fi0#46np^atwwdn%@m=n0(&1v$z_8ys==a'

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
    'UserAuthentication',
    'productstemplate',
    'payment',
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

ROOT_URLCONF = 'Online_Gadget_Store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
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

WSGI_APPLICATION = 'Online_Gadget_Store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# for online server (requirements)
# Django==3.2.4
# djongo==1.3.6
# pymongo==3.12.1


# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
#             'NAME': 'MyDatabase',
#             'ENFORCE_SCHEMA': False,
#             'CLIENT': {
#                 'host': 'mongodb+srv://admin:123@cluster0.ypkdud7.mongodb.net/?retryWrites=true&w=majority'
#             }
#         }
# }


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_DIR = Path.joinpath(BASE_DIR, 'statics')

STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_URL = 'media/'
MEDIA_ROOT = 'medias'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'   # for SMTP Sever   # EMAIL_HOST_PASSWORD is requird
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sunnyvai110@gmail.com'
EMAIL_HOST_PASSWORD = 'tkltktqwtqvmgsqf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#  from Stripe account 
STRIPE_SECRET_KEY = 'sk_test_51L0sl6E7kjWeybN5vvi99UYgfnrtDw9kUtsetqiFChkKL037bpzUCX7bfreXE97n1FCI51QCXNzXQV6QE6DX76gQ00VX4kNELY'
STRIPE_PUBLISH_KEY = 'pk_test_51L0sl6E7kjWeybN5sAWCpKCLDmTYB0Izyfdp9Y61EyXOFDNzx8xYkAeXdU06vx3XeoqwB7CF5GazzyyPG4i5miZ000fR7WEXLV'

WEB_HOOK_SECRETE_KEY ='whsec_1889e3f2b5edc5a90e7ae76233c5564dd4cad33fef9a64e546d134d5cedf31ff'