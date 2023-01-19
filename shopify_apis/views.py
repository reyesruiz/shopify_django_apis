'''
views
'''
import sys
from django.http import HttpResponse
from django.http import JsonResponse
from com_digitalruiz_my_logger import my_logger
from com_digitalruiz_shopify_tools import shopify_tools
from com_digitalruiz_shopify_apis import shopify_apis as shopify

LOGGER = my_logger.set_logger(module_name=sys.argv[0], loglevel='INFO')

def index(request):
    '''
    index page
    '''
    LOGGER.info(request)
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    '''
    test page
    '''
    LOGGER.info(request)
    return HttpResponse("This is a test")

def products(request):
    '''
    api to get all products
    '''
    LOGGER.info(request)
    products_data = shopify.get_all_products()
    return JsonResponse(products_data, safe=False)

def product(request, product_id=0):
    '''
    return product object
    '''
    LOGGER.info(request)
    if product_id == 0 or not product_id:
        return HttpResponse("Please provide a product id in the url")
    shopify_product_data = shopify.get_shopify_product_data(product_id)
    if shopify_product_data:
        return JsonResponse(shopify_product_data, safe=False)
    return None

def check_barcodes(request):
    '''
    Function to check if there are any duplicate barcodes
    '''
    LOGGER.info(request)
    response = shopify_tools.check_barcodes()
    return HttpResponse(response)

def generate_barcodes(request, product_id=0):
    '''
    Function to generate barcodes
    '''
    LOGGER.info(request)
    if product_id == 0 or not product_id:
        return HttpResponse("Please provide a product id in the url")
    response = shopify_tools.generate_barcodes(product_id)
    print(response)
    if response:
        return JsonResponse(response)
    return HttpResponse(status=500)
