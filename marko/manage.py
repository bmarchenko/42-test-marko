#!/usr/bin/env python
from django.core.management import execute_manager
import os.path
import sys
base = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(base, 'apps/'))
sys.path.insert(0, base)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
try:
    import settings
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the \
    directory containing %r. It appears you've customized things.\nYou'll \
    have  to run django-admin.py, passing it your settings \
    module.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
