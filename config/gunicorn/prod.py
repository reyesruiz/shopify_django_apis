"""Gunicorn *production* config file"""

import os
import multiprocessing

# pylint: disable=invalid-name
# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "shopify_django_apis.wsgi:application"
# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1
# The socket to bind
bind = '0.0.0.0:' + os.environ.get('SHOPIFY_APIS_PORT')
# Write access and error info to /var/log
accesslog = "/var/log/gunicorn/shopify-apis." + \
        os.environ.get('shopify_store_name') + \
        os.environ.get('domain_name') + ".access.log"
errorlog = "/var/log/gunicorn/shopify-apis." + \
        os.environ.get('shopify_store_name') + \
        os.environ.get('domain_name') + ".error.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/shopify-apis." + \
        os.environ.get('shopify_store_name') + \
        os.environ.get('domain_name') + ".pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True
