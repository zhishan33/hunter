# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from flask import make_response, Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from hunter.utils.wrappers import require_login
from hunter.utils.logger import PrintLog
from hunter.utils.models import User
from hunter import app
from hunter.utils.form import RegisterForm


from flask import render_template


@app.route('/index')
def page_not_found():
    session['is_login'] = True
    return render_template('hunter_index.html')


@app.route('/about')
def about():
    return render_template('hunter_about.html')


@app.route('/service')
def service():
    return render_template('hunter_service.html')


@app.route('/form')
# @require_login
def form():
    # import pdb
    # pdb.set_trace()
    PrintLog.print_log(s='sadfasdf')
    return render_template('hunter_form.html')
