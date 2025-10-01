from .base import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "avazcoder.uz").split(",")

# ================= additionally information =================
CSRF_TRUSTED_ORIGINS = ["https://" + h for h in ALLOWED_HOSTS if h]
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
