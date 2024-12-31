from our_wedding.settings.common import *

# from camiyaqui.settings.aws_credentials import *

# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, '../../emails')

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "camiaqui",
        "USER": "deven",
        "PASSWORD": "728000",
    }
}

WEBSITE_URL = "http://localhost:8000"

LOGIN_TOKEN_TIMEOUT_DAYS = 1


# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
