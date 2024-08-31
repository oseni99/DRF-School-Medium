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
