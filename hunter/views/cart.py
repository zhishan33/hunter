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


# 购物车页面
@app.route('/cart/index')
@require_login
def cart_index():
    return render_template('hunter_cart_index.html')


# 添加商品至购物车
@app.route('/cart/add', methods=['POST'])
@require_login
def cart_add():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'添加购物车失败,请稍后再试！', 'status': 200}))


# 购物车搜索
@app.route('/cart/search', methods=['POST'])
@require_login
def cart_search():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'查询失败,请稍后再试！', 'status': 200}))


# 修改购物车商品数量
@app.route('/cart/update', methods=['POST'])
@require_login
def cart_update():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'修改产品数量失败,请稍后再试！', 'status': 200}))


# 从购物车删除商品
@app.route('/cart/delete', methods=['POST'])
@require_login
def cart_delete():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'删除产品失败,请稍后再试！', 'status': 200}))


# 生成购物车支付链接
@app.route('/cart/pay', methods=['POST'])
@require_login
def cart_pay():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'生成订单失败,请稍后再试！', 'status': 200}))
