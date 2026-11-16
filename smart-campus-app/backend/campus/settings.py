import os
from pathlib import Path
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-local-key")
DEBUG = os.getenv("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
 "django.contrib.contenttypes", "django.contrib.auth",
 "rest_framework", "corsheaders", "api",
]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware",
 "django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "campus.urls"
TEMPLATES = []
WSGI_APPLICATION = "campus.wsgi.application"
DATABASES = {"default": dj_database_url.config(
 default=os.getenv("DATABASE_URL", "sqlite:///db.sqlite3"))}
CORS_ALLOW_ALL_ORIGINS = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
