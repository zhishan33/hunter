# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from flask import make_response, Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from hunter.utils.wrappers import require_login
from hunter.utils.logger import PrintLog
from hunter import app
from hunter.utils.form import RegisterForm
from hunter.utils.exception import LocalException
from hunter.utils.models import User
import json
from hunter.utils.wrappers import require_login


# 个人信息详情
@app.route('/address/index')
def address_index():
    return render_template('hunter_about.html')

