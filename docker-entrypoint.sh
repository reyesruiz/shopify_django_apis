#!/bin/bash
python manage.py migrate 
gunicorn --config /usr/src/app/config/gunicorn/prod.py
sleep 1
tail -f /var/log/gunicorn/shopify-apis.los-vaqueros-wester-wear.digitalruiz.com.access.log /var/log/gunicorn/shopify-apis.los-vaqueros-wester-wear.digitalruiz.com.error.log 
exec "$@"
