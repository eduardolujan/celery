from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^sum/<int:a>/<int:b>$', testsum, name='testsum')
]
