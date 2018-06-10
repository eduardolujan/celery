#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'distributed_app.settings')
except:
    pass
app = Celery('distributed_app')  # Nota 1
app.config_from_object('django.conf:settings', namespace='CELERY')  # Nota 2
app.autodiscover_tasks()
app.conf.update(
    BROKER_URL='redis://localhost:6379/5',
)


#celery worker -A distributed_task_queue.celery --loglevel=info