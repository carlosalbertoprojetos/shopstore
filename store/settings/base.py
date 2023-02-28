import os
from pathlib import Path

# import django_heroku


BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = 'django-insecure-)m@(j@s9pdl+8d0zyf3pzuzcb7_3sp$=ps%7!o%u6h)x16x%-v'


DEBUG = True


ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # necessário para o django-allauth:
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # apps de terceiros
    'crispy_forms',
    'crispy_bootstrap4',
    'localflavor',

    # # login com google/Facebook
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',

    # meus apps
    'financial',
    'order',
    'product',
    'register'
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


ROOT_URLCONF = 'store.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'store.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR / 'db.sqlite3')),
    }
}


if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}


DATE_FORMAT = ["%d/%m/%Y"]
DATE_INPUT_FORMATS = ('%d/%m/%Y','%d-%m-%Y','%Y-%m-%d')
DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True


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


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = ''
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = '2525'


# # necessário para o django-allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Método de autenticação: email
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# Email obrigatório
ACCOUNT_EMAIL_REQUIRED = True
# Email único
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_CONFIRM_EMAIL_ON_GET=False

# confirmação de cadastro por email / loga somente após esta confirmação
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# redirecionar ao clicar no link de confirmação de email
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/accounts/login/'

ACCOUNT_LOGOUT_ON_GET = True

# apis contas sociais
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },

    # 'facebook': {
    #     'METHOD': 'oauth2',
    #     'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
    #     'SCOPE': ['email', 'public_profile'],
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'INIT_PARAMS': {'cookie': True},
    #     'FIELDS': [
    #         'id',
    #         'first_name',
    #         'last_name',
    #         'middle_name',
    #         'name',
    #         'name_format',
    #         'picture',
    #         'short_name'
    #     ],
    #     'EXCHANGE_TOKEN': True,
    #     'LOCALE_FUNC': lambda request: 'pt-br',
    #     'VERIFIED_EMAIL': False,
    #     'VERSION': 'v7.0',
    # },
}


# LANGUAGE_CODE = 'pt-br'
LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'America/Sao_Paulo'
TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True



MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]


LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django-crispy-forms.
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Heroku
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# django_heroku.settings(locals())