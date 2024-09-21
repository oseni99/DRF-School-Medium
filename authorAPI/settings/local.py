from .base import env
from .base import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="sNiIaF71HIdsWdlOPOTc2mfS8rExMrpbY4C3esmao2hdRqPm1RA",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]


EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="localhost")
EMAIL_PORT = env("EMAIL_PORT", default=25)
DEFAULT_FROM_EMAIL = "kingosenitosin@gmail.com"
DOMAIN = env("DOMAIN", default="localhost:8000")
SITE_NAME = "Campus Voice"
