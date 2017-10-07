# -*- coding: utf-8 -*-

"""
Created by yangshuanglong@wecash.net on 2017/10/5
"""


def application(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ["hello!"]
