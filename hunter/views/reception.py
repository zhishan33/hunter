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
from hunter.utils.models import User

appid = 'wx88571edcc2b11194'
appsecret = '9a189a86532a5cf99f1ba5782571c4ac'
import urllib2
# 工作台首页
@app.route('/index')
def reception_index():
    '''
    openid	用户的唯一标识
    nickname	用户昵称
    sex	用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
    province	用户个人资料填写的省份
    city	普通用户个人资料填写的城市
    country	国家，如中国为CN
    headimgurl	用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表640*640正方形头像），用户没有头像时该项为空。若用户更换头像，原有头像URL将失效。
    privilege	用户特权信息，json 数组，如微信沃卡用户为（chinaunicom）
    unionid	只有在用户将公众号绑定到微信开放平台帐号后，才会出现该字段。详见：获取用户个人信息（UnionID机制）
    '''
    code = request.args.get('code', '')
    if not session.get('is_login', False):
        if code != '':
            # 获取用户access_token
            url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' % (
                appid, appsecret, code)
            res = urllib2.urlopen(url)
            resdict = json.load(res)

            openid = resdict.get('openid', '')
            access_token = resdict.get('access_token', '')
            print('openid: %s   accesstoken:%s' % (openid, access_token))
            # 获取微信用户信息
            user_url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN' % (
                access_token, openid)
            user_info = urllib2.urlopen(user_url)

            print('userinfo:%s' % user_info)
            user_info_dict = json.load(user_info)
            nickname = user_info_dict.get('nickname', 'WechatUser')
            sex = user_info_dict.get('sex', '')
            province = user_info_dict.get('province', '')
            city = user_info_dict.get('city', '')
            country = user_info_dict.get('country', '')
            headimgurl = user_info_dict.get('headimgurl', '')
            privilege = user_info_dict.get('privilege', '')
            unionid = user_info_dict.get('unionid', '')
            # 检查账户是否已经存在odoo数据库中,不存在则创建
            ids = User().search(domain=[('login', '=', openid)])
            if not ids:
                newuser = User().create(login=openid, password='', name=nickname)
                session['uid'] = newuser
            else:
                session['uid'] = ids[0]
            session['is_login'] = True
            session['openid'] = openid
            session['access_token'] = access_token
            print(user_info_dict)
        else:
            session['is_login'] = False
            # ids = User().search(domain=[('login', '=', 'test')])
            #     if not ids:
            #         User().create(login='test', password='', name='wechatuser')
            #     else:
            #         print(ids)
            #     return render_template('hunter_index.html')

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
