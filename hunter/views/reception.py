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


# 工作台首页
@app.route('/index')
def reception_index():
    return render_template('hunter_index.html')


# 第一排------------------------------------------
# 扫一扫
@app.route('/reception/scan', methods=['POST'])
@require_login
def reception_scan():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 到付码
@app.route('/reception/paycode', methods=['POST'])
@require_login
def reception_paycode():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 第一排+++++++++++++++++++++++++++++++++++++++++++++++


# 周边
@app.route('/reception/surround', methods=['POST'])
@require_login
def reception_surround():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 九宫格-----------------------------------------------
# 充值
@app.route('/reception/recharge', methods=['POST'])
@require_login
def reception_recharge():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 还款
@app.route('/reception/repayment', methods=['POST'])
@require_login
def reception_repayment():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 消费
@app.route('/reception/consumption', methods=['POST'])
@require_login
def reception_consumption():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 卡次
@app.route('/reception/card', methods=['POST'])
@require_login
def reception_card():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 活动
@app.route('/reception/activity', methods=['POST'])
@require_login
def reception_activity():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 优惠券
@app.route('/reception/coupon', methods=['POST'])
@require_login
def reception_coupon():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 签到
@app.route('/reception/check', methods=['POST'])
@require_login
def reception_check():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))
