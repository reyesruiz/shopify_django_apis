# shopify_django_apis

Django application to communicate with Shopify api endpoints. I created this as intermediate step between a react application and Shopify, since I am more proficient in python, so it is easier to manipulate data there.

# Author

Reyes Ruiz
reyes@digitalruiz.com

# Installation

Using ubuntu 22.01 LTS version

**Update ubuntu**

```
sudo apt update && sudo apt -y upgrade && sudo reboot
```

**Install python and some requirements**

```
sudo apt install python3 python3-pip python-is-python3 python3-venv
```

**Create gunicorn log and run folders**

```
sudo mkdir -pv /var/{log,run}/gunicorn/
```

**Change ownership of folder to the user where you are running the application: Example ubuntu**

```
sudo chown ubuntu:ubuntu /var/{log,run}/gunicorn/
```

**Clone git hub repository**

```
git clone https://github.com/reyesruiz/shopify_django_apis.git
```

**Create a virtual environment**

```
python -m venv test
source test/bin/activate
```

**Change to project directory**

```
cd shopify_django_apis
```

**Install requirements from the project**

```
pip install --upgrade -r requirements.txt
```

**Install gunicorn from pip**

```
pip install --upgrade gunicorn
```

**Environment file needed for web app to run correctly**

```
vim test.env
```

**File contents**

```
export shopify_store_name='{shopify store name}'
export shopify_admin_api_version='{shopify api version}'
export shopify_access_token='{shopify access token}'
export shopify_deafult_location='{default shopify location id for inventory purposes}'
export ALLOWED_HOSTS='{allowed hosts comma separated'
export DJANGO_DEBUG='True or False'
export SECRET_KEY='secret key for django'
export WEB_BIND='0.0.0.0:8000'
```

**Variables explanation**
|Variable name|Description |Example|Reference|
|--|--|--|--|
|shopify_store_name|Shopify store name: the name without the myshopify.com|my-shopify-store-name||
|shopify_admin_api_version|Shopify API Version|2023-01|<https://shopify.dev/api/admin-rest/latest/resources/product|>
|shopify_access_token|Shopify access token to be able to communicate with shopify apis|shpat_..............|<https://www.shopify.com/partners/blog/17056443-how-to-generate-a-shopify-api-token|>
|shopify_deafult_location|Default shopify inventory location id to work with. No required as right now, you can set it to 0|3267254135673||
|ALLOWED_HOSTS|Allowed hosts for django application to work values in comma separated|my-shopify-django-app.mydomainname.com,localhost,127.0.0.1|<https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts|>
|DJANGO_DEBUG|Debug settings for django, for production set to False, for development set to True|False|<https://docs.djangoproject.com/en/4.1/ref/settings/#debug|>
|SECRET_KEY|Django secret key, check below on how to generate one|ccn)gl6%%o5c9fi$z32ssl954hs4awz$i%k5uyvwodb9vu65z=|<https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key|>
|WEB_BIND|Address bind for gunicorn to run on, 0.0.0.0 means all ips, and after we set the port we want our app to be served from like port 8000|0.0.0.0:8000|<https://docs.gunicorn.org/en/stable/settings.html#server-socket|>

**Generate a secret key**

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

```
ccn)gl6%%o5c9fi$z32ssl954hs4awz$i%k5uyvwodb9vu65z=
```

**Source the environment file you created**

```
source test.env
```


**Apply migrations to Django project**

```
python manage.py migrate
```

**Create auth token to be used in get calls**
```
python manage.py createsuperuser --username shopifystorename --email shopifystorename@example.com
```
set to uniqe user name for your specific store, will ask for a password too, that is used to get the token via web endpoint, but will not use it this time

```
python manage.py drf_create_token shopifystorename
```
It will generate a token, save it to a a safe place, this is what we will be using for authorization to access our apis.

**Authorization header**
The header that need to send to authenticate with our endpoints is:
|Header|Value|
|--|--|
|Authorization|Token mygeneratedtoken'|

Example:
curl http://127.0.0.1:8000/shopify_apis/ -H 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'

**Run the server**
Development

```
gunicorn -c config/gunicorn/dev.py
```

Production

```
gunicorn -c config/gunicorn/prod.py
```

If everything went right, when you tail /var/log/gunicorn/dev.log or /var/log/gunicorn/error.log you will be able to see it has been started correctly, you can access it via <http://{host-ip}:8000>
You will get an error about ip not being added in ALLOWED_HOSTS.

# Create another site

**change back to previous directory**

```
cd ..
```

**Deactivate current enviroment**

```
deactivate
```

**Re run all the steps from above with your new configurations starting from "Create a virtual environment"**

## Things To do

 1. Update this document to include Nginx configurations, to serve via HTTPS
 2. Once it is running make it survive a reboot