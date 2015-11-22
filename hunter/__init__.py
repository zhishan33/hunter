# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask

app = Flask(__name__)

from hunter.views.cart import cart_index
from hunter.views.order import *
from hunter.views.product import *
from hunter.views.reception import *
from hunter.views.user import *