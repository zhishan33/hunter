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


# 订单列表页面
@app.route('/order/index')
@require_login
def order_index():
    return render_template('hunter_order.html')


# 订单详情页面
@app.route('/order/detail')
@require_login
def order_detail():
    return render_template('hunter_order.html')


# 搜索订单
@app.route('/order/search', methods=['POST'])
@require_login
def order_search():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'搜索失败,请稍后再试！', 'status': 200}))


# 订单删除
@app.route('/order/delete', methods=['POST'])
@require_login
def order_delete():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'删除订单失败,请稍后再试！', 'status': 200}))
