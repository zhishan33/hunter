# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import request, abort, session
from flask import make_response
import json


def require_login(fun):
    def wrapper(*args, **kwargs):
        if session.get('is_login', False):
            return fun(*args, **kwargs)
        else:
            return make_response(json.dumps({'flag': 'False', 'status': 401, 'next': '/login','origin':request.url}))

    return wrapper
