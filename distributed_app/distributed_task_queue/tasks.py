#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import, unicode_literals
from .celery_app_setup import app

@app.task
def celery_task_sum(x, y):
    print('El resultado es {}'.format(x+y))
    return x + y


@app.task
def celery_task_rest(x, y):
    return x - y