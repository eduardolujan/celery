from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def testsum(request, a, b):
    return HttpResponse(json.dumps({'response': '{a} + {b} sended to queue'.format(a=a, b=b)}))
