from django.shortcuts import render
from django.http import HttpResponse
import json
from distributed_task_queue.tasks import celery_task_sum
from decimal import Decimal
# Create your views here.

def testsum(request, a, b):
    a = int(a)
    b = int(b)
    celery_task_sum(a, b)

    r = celery_task_sum.apply_async((Decimal(a), Decimal(b)), serializer='json')
    return HttpResponse(json.dumps({'response': '{a} + {b} sended to queue'.format(a=a, b=b)}))


def test(request):
    return HttpResponse('OK')
