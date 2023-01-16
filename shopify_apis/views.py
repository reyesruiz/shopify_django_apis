'''
views
'''
from django.http import HttpResponse
from django.http import JsonResponse
from com_digitalruiz_shopify_apis import shopify_apis as shopify

def index(request):
    '''
    index page
    '''
    print(request)
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    '''
    test page
    '''
    print(request)
    return HttpResponse("This is a test")

def products(request):
    '''
    api to get all products
    '''
    print(request)
    products = shopify.get_all_products()
    return JsonResponse(products, safe=False)

def product(request, id=0):
    if id == 0 or not id:
        return HttpResponse("Please provide a product id in the url")
    product_id = id
    shopify_product_data = shopify.get_shopify_product_data(product_id)
    if shopify_product_data:
        return JsonResponse(shopify_product_data, safe=False)
