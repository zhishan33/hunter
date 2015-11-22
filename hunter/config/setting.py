# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import xmlrpclib

SERVER_URL = 'http://121.41.112.103:8069/xmlrpc/'
DB = 'shop'
COMMON_URL = SERVER_URL + 'common'
OBJECT_URL = SERVER_URL + 'object'



common = xmlrpclib.ServerProxy(COMMON_URL)
obj = xmlrpclib.ServerProxy(OBJECT_URL)
