# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def first_generate(redis=None, prefix='unknown', base=50000, first=1000):
    maxid_key = '%s:maxid' % prefix
    code_key = '%s:code' % prefix
    is_exist = redis.exists(maxid_key)
    if is_exist: return False

    maxid = base + first
    redis.set(maxid_key, maxid)

    code = range(base, base+first)
    redis.sadd(code_key, *code)
    return True

def incr_generate(redis=None, prefix='unknown', incr=1000, min_count=100):
    maxid_key = '%s:maxid' % prefix
    code_key = '%s:code' % prefix
    count = redis.scard(code_key)
    if count > min_count:
        return False

    origin_maxid = int(redis.get(maxid_key))
    maxid = origin_maxid + incr
    redis.set(maxid_key, maxid)

    code = range(origin_maxid, maxid)
    redis.sadd(code_key, *code)
    return True

def get_invcode(redis=None, prefix='unknown'):
    code_key = '%s:code' % prefix
    return int(redis.spop(code_key))
