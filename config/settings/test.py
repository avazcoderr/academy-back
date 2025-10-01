from .base import *

DEBUG = False
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('DB_NAME', 'test_db'),
    'USER': os.environ.get('DB_USER', 'test_user'),
    'PASSWORD': os.environ.get('DB_PASSWORD', 'test_password'),
    'HOST': os.environ.get('DB_HOST', 'localhost'),
    'PORT': os.environ.get('DB_PORT', '5432'),
}
