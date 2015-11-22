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
import json
from hunter.utils.wrappers import require_login


# 个人信息详情
@app.route('/user/info/index')
@require_login
def user_detail():
    return render_template('hunter_user_index.html')


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
