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
import urllib2

# 个人信息详情
@app.route('/user/info/index')
# @require_login
def user_detail():
    if not session.get('is_login', False):
        return render_template('hunter_user_login.html')
    else:
        info = User().read([session['uid']])
    return render_template('hunter_user_index.html', user=info[0])


# 用户openid
@app.route('/user/wgateid/<wgateid>', methods=['POST', 'GET'])
def getopenid(wgateid):
    url = 'http://www.weixingate.com/wgate_user.php?wgateid=%s' % 'oXQ7gt6aI0oPhV8k5krigVCtpko4'
    res = urllib2.urlopen(url)
    result = res.read()
    return result


@app.route('/user/login', methods=['POST', 'GET'])
def user_login():
    try:
        if request.method == 'POST':
            username = request.form.get('login', '')
            password = request.form.get('password', '')
            origin_url = request.form.get('origin_url', '/index')
            id = User().login_user(login=username, password=password)
            if not id:
                raise LocalException('用户名或密码错误')
            else:
                session['is_login'] = True
                session['uid'] = id
        return make_response(json.dumps({'flag': 'True', 'msg': '', 'origin_url': origin_url}))
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message}))
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': u'登陆失败,请稍后再试'}))


@app.route('/user/logout', methods=['POST', 'GET'])
def user_logout():
    session['is_login'] = False
    session['uid'] = None
    return render_template('hunter_index.html')


@app.route('/user/register/page', methods=['POST', 'GET'])
def user_register_page():
    return render_template('hunter_user_register.html')


@app.route('/user/register', methods=['POST', 'GET'])
def user_register():
    try:
        if request.method == 'POST':
            origin_url = request.form.get('origin_url', '/index')
            username = request.form.get('login', '')
            password = request.form.get('password', '')
            repassword = request.form.get('repassword', '')
            if username == '':
                raise LocalException(u'用户名不可为空')
            if password != repassword:
                raise LocalException(u'两次密码不匹配')
            if len(password) < 6:
                raise LocalException(u'密码长度不可小于6位')
            ids = User().search([('login', '=', username)])
            if ids:
                raise LocalException(u'用户已经存在')
            else:
                import pdb

                pdb.set_trace()
                newuser = User().create(login=username, password=password, name=username)
            session['is_login'] = True
            session['uid'] = newuser
            return make_response(json.dumps({'flag': 'True', 'msg': '', 'origin_url': origin_url}))
        else:
            raise LocalException(u'非法操作')
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message}))
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': u'注册失败,请稍后再试'}))


# 用户信息更新表单页
@app.route('/user/info/form')
@require_login
def user_info_form():
    return render_template('hunter_user_info_form.html')


# 修改用户信息
@app.route('/user/info/update', methods=['POST'])
@require_login
def user_update():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'修改产品数量失败,请稍后再试！', 'status': 200}))


# 用户地址表单页
@app.route('/user/address/form')
@require_login
def user_address_form():
    return render_template('hunter_user_address_form.html')


# 添加用户地址
@app.route('/user/address/add', methods=['POST'])
@require_login
def user_address_add():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'修改产品数量失败,请稍后再试！', 'status': 200}))


# 删除用户地址
@app.route('/user/address/delete', methods=['POST'])
@require_login
def user_address_delete():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'修改产品数量失败,请稍后再试！', 'status': 200}))


# 更新用户地址
@app.route('/user/address/update', methods=['POST'])
@require_login
def user_address_update():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'修改产品数量失败,请稍后再试！', 'status': 200}))
