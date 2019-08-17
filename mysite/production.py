# --------------------------------------------------------------------------- #
# Course: PYTHON 230: Internet Programming With Python
# Script Title: 
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-08-15, Initial release
# --------------------------------------------------------------------------- #

import dj_database_url
from .settings import *
import os

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
    }

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get('SECRET_KEY')
