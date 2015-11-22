# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from functools import wraps
from flask import request, abort, session
from flask import make_response
import json


def require_login(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if session.get('is_login', False):
            return fun(*args, **kwargs)
        else:
            return fun(*args, **kwargs)
            return make_response(json.dumps({'flag': 'False', 'status': 401, 'next': '/login', 'origin': request.url}))

    return wrapper
