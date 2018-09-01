"""
Django settings for fittrak project.
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG")

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

HASHIDS_SALT = os.getenv("DJANGO_HASHIDS_SALT")

# Allow handling by CIDR middleware
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "registration",  # Must appear before admin for templates
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third party
    "django_extensions",
    "graphene_django",
    "webpack_loader",
    "corsheaders",
    # Ours
    "users",
    "workouts",
    "stats",
]

MIDDLEWARE = [
    "allow_cidr.middleware.AllowCIDRMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "fittrak.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["fittrak/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "fittrak.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE") or "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Patch the DB to be sqlite in test env
if "test" in sys.argv:
    defaults = {"ENGINE": "django.db.backends.sqlite3", "NAME": "fittrak_test"}

    DATABASES["default"] = defaults

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
    os.path.join(BASE_DIR, "assets", "bundles"),
]

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SITE_ID = 1

# Temporarily use console backend for activation emails to avoid connection
# refused issues.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

GRAPHENE = {
    "SCHEMA": "fittrak.schema.schema",
    "MIDDLEWARE": ["graphene_django.debug.DjangoDebugMiddleware"],
}

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
    }
}

AUTH_USER_MODEL = "users.User"

# Registration conf
ACCOUNT_ACTIVATION_DAYS = 3
REGISTRATION_AUTO_LOGIN = True
SIMPLE_BACKEND_REDIRECT_URL = "/"
REGISTRATION_OPEN = True

CSRF_HEADER_NAME = "x-csrftoken"
CSRF_USE_SESSIONS = False  # Will use cookie

X_FRAME_OPTIONS = "DENY"
# Need SSL
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Email setup, see env file
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")

# Production override
# TODO: should really be separate settings files
if not DEBUG:
    ALLOWED_HOSTS = []
    ALLOW_CIDR_NETS = ["10.0.0.0/24", "10.1.1.0/24"]
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ALLOW_CREDENTIALS = False
