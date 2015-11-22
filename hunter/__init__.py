# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask
app = Flask(__name__)

from hunter.view import index

