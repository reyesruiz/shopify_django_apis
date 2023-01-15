'''
views
'''
from django.http import HttpResponse

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
