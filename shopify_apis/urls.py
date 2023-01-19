'''
Setting urls
'''
from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('test', views.test, name='test'),
        path('products', views.products, name='products'),
        path('product', views.product, name='product'),
        path('product/', views.product, name='product'),
        path('product/<str:product_id>', views.product, name='product'),
        path('check_barcodes', views.check_barcodes, name='check_barcodes'),
        path('generate_barcodes', views.generate_barcodes, name='generate_barcodes'),
        path('generate_barcodes/', views.generate_barcodes, name='generate_barcodes'),
        path('generate_barcodes/<str:product_id>', views.generate_barcodes,
             name='generate_barcodes'),
]
