import pathlib
import os
import sys
import shutil
from django.core.wsgi import get_wsgi_application

BASE_DIR = pathlib.Path().parent.resolve()

# ruta a nuestro proyecto de django
djangoproject_home = os.path.join(BASE_DIR, 'portin')

sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = get_wsgi_application()

from portin.apps.profiles.models import Profile
from django.conf import settings

CUSTOM_APPS = settings.CUSTOM_APPS

for app in CUSTOM_APPS:
    app = app.split('.')[-1]
    ruta = '{}/portin/apps/{}/migrations'.format(BASE_DIR, app)
    print (ruta)

    # eliminamos la carpeta migraciones
    try:
        shutil.rmtree(ruta)
    except:
        pass

    # la volvemos a crear
    os.makedirs(ruta)
    # y cargamos el archivo init dentro de esa ruta
    archivo = open(ruta+'/__init__.py', 'w')
    archivo.close()

print ('Migraciones eliminadas correctamente :)')