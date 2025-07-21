import os
from app import app # ¡IMPORTACIÓN RELATIVA Y SIMPLE!

# Esto expone la aplicación para que Gunicorn la encuentre.
# El nombre 'application' es una convención común para gunicorn.
application = app
