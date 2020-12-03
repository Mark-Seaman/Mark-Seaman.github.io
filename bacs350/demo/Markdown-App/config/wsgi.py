# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

## assuming your django settings file is at '/home/markseaman/BACS-350/bacs350/bacs350/settings.py'
## and your manage.py is is at '/home/markseaman/BACS-350/bacs350/manage.py'
path = '/home/markseaman/BACS-350/bacs350'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bacs350.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
