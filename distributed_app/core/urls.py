from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^suma/(?P<a>\d+)/(?P<b>\d+)/?$', testsum),
    url(r'^test/?$', test)
]
