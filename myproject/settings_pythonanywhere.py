"""
Django settings for PythonAnywhere deployment.
"""

from .settings import *

# Override settings for PythonAnywhere
DEBUG = False

# PythonAnywhere specific settings
ALLOWED_HOSTS = [
    'YOUR_USERNAME.pythonanywhere.com',
    'www.YOUR_USERNAME.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

# Static files configuration for PythonAnywhere
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 31536000
X_FRAME_OPTIONS = 'DENY'

# Disable HTTPS redirect for PythonAnywhere (they handle it)
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Database configuration (use SQLite for free tier)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files storage
STATICFILES_STORAGE = 'django.contrib.static.storage.StaticFilesStorage'
