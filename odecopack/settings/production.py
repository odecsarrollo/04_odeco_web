from .base import *

DEBUG = False
########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    (os.environ['ADMIN_NAME'], os.environ['ADMIN_EMAIL']),
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'storages',
)

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_HOST = 's3-us-west-2.amazonaws.com'
AWS_IS_GZIPPED = True

GZIP_CONTENT_TYPES = (
    "application/atom+xml",
    "application/javascript",
    "application/json",
    "application/ld+json",
    "application/manifest+json",
    "application/rdf+xml",
    "application/rss+xml",
    "application/schema+json",
    "application/vnd.geo+json",
    "application/vnd.ms-fontobject",
    "application/x-font-ttf",
    "application/x-javascript",
    "application/x-web-app-manifest+json",
    "application/xhtml+xml",
    "application/xml",
    "font/eot",
    "font/opentype",
    "image/bmp",
    "image/webp",
    "image/jpg",
    "image/png",
    "image/svg+xml",
    "image/vnd.microsoft.icon",
    "image/x-icon",
    "text/cache-manifest",
    "text/css",
    "text/html",
    "text/javascript",
    "text/plain",
    "text/vcard",
    "text/vnd.rim.location.xloc",
    "text/vtt",
    "text/x-component",
    "text/x-cross-domain-policy",
    "text/xml"
)

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=31536000',
}

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

########## END STATIC FILE CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.environ['DB_ENGINE'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
########## END DATABASE CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = os.environ['EMAIL_HOST']

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = os.environ['EMAIL_PORT']

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = str_to_bool(os.environ['EMAIL_USE_TLS'])

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = os.environ["SERVER_EMAIL"]

EMAIL_USE_SSL = str_to_bool(os.environ["EMAIL_USE_SSL"])

DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]
########## END EMAIL CONFIGURATION


########MAILCHIMP##############
MAILCHIMP_API_KEY = os.environ["MAILCHIMP_API_KEY"]
MAILCHIMP_USERNAME = os.environ["MAILCHIMP_USERNAME"]
MAILCHIMP_LIST_ID = os.environ["MAILCHIMP_LIST_ID"]

########## CACHE ###################
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://%s:%s/1' % (os.environ['REDIS_HOST'], int(os.environ['REDIS_PORT'])),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'COMPRESSOR_CLASS': 'redis_cache.compressors.BZip2Compressor',
        }
    }
}
IMAGEKIT_CACHE_BACKEND = 'default'
IMAGEKIT_CACHE_PREFIX = 'imagekit:'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = "default"
SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = None
SOLO_CACHE_PREFIX = 'solo'
GOOGLE_RECAPTCHA_SECRET_KEY = os.environ["GOOGLE_RECAPTCHA_SECRET_KEY"]
