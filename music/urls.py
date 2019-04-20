from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$',views.detail,name= 'detail'),
    url(r'^(?P<product_id>[0-9]+)/added$',views.addInCart,name='addInCart'),
]
