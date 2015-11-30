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


# 产品列表页面
@app.route('/product/index')
def product_index():
    return render_template('hunter_product_index.html')


# 产品搜索
@app.route('/product/search', methods=['POST'])
def product_search():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'搜索失败,请稍后再试！', 'status': 200}))  # 添加商品至购物车


# 产品的分类列表
@app.route('/product/category', methods=['POST'])
def product_category():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'获取产品分类失败,请稍后再试！', 'status': 200}))  # 添加商品至购物车


# 产品分享链接
@app.route('/product/share', methods=['POST'])
def product_share():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        PrintLog.print_normal_log(request.form)
        return make_response(json.dumps({'flag': 'False', 'msg': u'产品分享失败,请稍后再试！', 'status': 200}))


# 推荐产品列表
@app.route('/product/recommend', methods=['POST'])
def product_recommend():
    try:
        pass
    except LocalException as e:
        return make_response(json.dumps({'flag': 'False', 'msg': e.message, 'status': 200}))
    except Exception as e:
        return make_response(json.dumps({'flag': 'False', 'msg': u'获取推荐产品失败,请稍后再试！', 'status': 200}))


# 产品详情页面
@app.route('/product/detail/<int:id>', methods=['POST','GET'])
def product_detail(id):
    return render_template('hunter_product_detail.html')