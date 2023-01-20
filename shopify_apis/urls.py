'''
Setting urls
'''
from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('test', views.Test.as_view(), name='test'),
        path('products', views.Products.as_view(), name='products'),
        path('product', views.Product.as_view(), name='product'),
        path('product/', views.Product.as_view(), name='product'),
        path('product/<str:product_id>', views.Product.as_view(), name='product'),
        path('check_barcodes', views.CheckBarcodes.as_view(), name='check_barcodes'),
        path('generate_barcodes', views.GenerateBarcodes.as_view(), name='generate_barcodes'),
        path('generate_barcodes/', views.GenerateBarcodes.as_view(), name='generate_barcodes'),
        path('generate_barcodes/<str:product_id>', views.GenerateBarcodes.as_view(),
             name='generate_barcodes'),
]
