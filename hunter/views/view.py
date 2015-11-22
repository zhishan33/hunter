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


@app.route('/<name>', methods=['POST', 'GET'])
def hello_world(name):
    return 'Hello there World! %s' % name


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do_the_login()
        print(request.__dict__)
        return str(request.__dict__)
    else:
        # show_the_login_form()
        print(request.__dict__.keys())
        return str(request.__dict__)


@app.route('/cookie')
def index():
    username = request.cookies.get('username')
    resp = make_response()
    resp.set_cookie('username', 'the username')
    return resp


from flask import abort, redirect, url_for


@app.route('/')
def redirext():
    return redirect(url_for('login'))


@app.route('/login')
def login404():
    abort(401)
    # this_is_never_executed()


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
