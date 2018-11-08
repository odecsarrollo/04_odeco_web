from .base import *

############### SECRET FILE
import json

# Normally you should not import ANYTHING from Django directly
# into your perfil, but ImproperlyConfigured is an exception. from django.core.exceptions import ImproperlyConfigured
# JSON-based secrets module
from django.core.exceptions import ImproperlyConfigured

with open("secretsLocal.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, variable, secrets=secrets):
    """ Get the environment setting or return exception """
    try:
        return secrets[setting][variable]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


############### END SECRET FILE

########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    (
        get_secret("ADMIN_1", "NAME"),
        get_secret("ADMIN_1", "EMAIL")
    ),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
########## END DEBUG CONFIGURATION

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"{{ secret_key }}"
########## END SECRET CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION

THIRD_PART_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PART_APPS

# ########## CACHE CONFIGURATION
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }
# ######### END CACHE CONFIGURATION

# ########## DATABASE CONFIGURATION
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': get_secret("DATABASE_LOCAL", "ENGINE"),
#         'NAME': get_secret("DATABASE_LOCAL", "NAME"),
#         'USER': get_secret("DATABASE_LOCAL", "USER"),
#         'PASSWORD': get_secret("DATABASE_LOCAL", "PASSWORD"),
#         'HOST': get_secret("DATABASE_LOCAL", "HOST"),
#         'PORT': get_secret("DATABASE_LOCAL", "PORT")
#     }
# }
# ########## END DATABASE CONFIGURATION

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend

# 'EMAIL_IS_LOCAL'
if not str_to_bool(get_secret("EMAIL_SERVER", "EMAIL_IS_LOCAL")):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = get_secret("EMAIL_SERVER", "EMAIL_HOST")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_secret("EMAIL_SERVER", "EMAIL_HOST_PASSWORD")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = get_secret("EMAIL_SERVER", "EMAIL_HOST_USER")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = get_secret("EMAIL_SERVER", "EMAIL_PORT")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = str_to_bool(get_secret("EMAIL_SERVER", "EMAIL_USE_TLS"))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = get_secret("EMAIL_SERVER", "SERVER_EMAIL")

EMAIL_USE_SSL = str_to_bool(get_secret("EMAIL_SERVER", "EMAIL_USE_SSL"))

DEFAULT_FROM_EMAIL = get_secret("EMAIL_SERVER", "DEFAULT_FROM_EMAIL")

GOOGLE_RECAPTCHA_SECRET_KEY = get_secret("RECAPTCHA", "GOOGLE_RECAPTCHA_SECRET_KEY")

########## END EMAIL CONFIGURATION

########MAILCHIMP##############
MAILCHIMP_API_KEY = get_secret("MAILCHIMP", "MAILCHIMP_API_KEY")
MAILCHIMP_USERNAME = get_secret("MAILCHIMP", "MAILCHIMP_USERNAME")
MAILCHIMP_LIST_ID = get_secret("MAILCHIMP", "MAILCHIMP_LIST_ID")

######### DEBUG TOOLBAR CONFIGURATION CONFIGURATION
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INTERNAL_IPS = '127.0.0.1'
######### END TOOLBAR CONFIGURATION CONFIGURATION


########## CACHE ###################
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'COMPRESSOR_CLASS': 'redis_cache.compressors.BZip2Compressor',
        }
    }
}
IMAGEKIT_CACHE_BACKEND = 'default'
IMAGEKIT_CACHE_PREFIX = 'imagekit-odeco:'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = "default"
SOLO_CACHE_TIMEOUT = None
SOLO_CACHE_PREFIX = 'sol'
SOLO_CACHE = 'default'
