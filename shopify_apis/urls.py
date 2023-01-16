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
        path('product/<str:id>', views.product, name='product'),
]
