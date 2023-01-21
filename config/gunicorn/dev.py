"""Gunicorn *development* config file"""
import os

# pylint: disable=invalid-name
# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "shopify_django_apis.wsgi:application"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = os.environ.get('WEB_BIND')
# Restart workers when code changes (development only!)
reload = True
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True
