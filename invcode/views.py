# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import simplejson
from django.http import HttpResponse
from .utils import first_generate, incr_generate, get_invcode
from redis_cache import get_redis_connection

def index(request):
    redis = get_redis_connection('redis')
    first_generate(redis)
    incr_generate(redis)
    code = get_invcode(redis)
    res = {
        'ret': 0,
        'code': code
    }
    return HttpResponse(simplejson.dumps(res), mimetype="application/json; charset=utf-8")
