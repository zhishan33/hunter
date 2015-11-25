# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import xmlrpclib
from hunter import session

SERVER_URL = 'http://www.hunteramos.com:8069/xmlrpc/'
DB = 'shop'
admin_login = 'admin'
admin_pwd = '1'
# SERVER_URL = 'http://127.0.0.1:8069/xmlrpc/'
# DB = 'admin'
# admin_login = 'admin'
# admin_pwd = 'a'
COMMON = xmlrpclib.ServerProxy(SERVER_URL + 'common')
OBJ = xmlrpclib.ServerProxy(SERVER_URL + 'object')
admin_uid = COMMON.login(DB, admin_login, admin_pwd)

print(admin_uid)
class BaseModel(object):
    def __init__(self, login, pwd):
        self.login = login
        self.pwd = pwd
        self.loginin()

    def loginin(self):
        uid = COMMON.login(DB, self.login, self.pwd)
        if uid:
            self.uid = uid
            self.is_login = True
        else:
            self.is_login = False
            return False
        return True

    def write(self, *args, **kwargs):
        pass

    def unlink(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass

    def search(self, *args, **kwargs):
        pass


class User(BaseModel):
    columns = ['login', 'passwd', 'email', 'name', 'street', 'province', 'credit', 'level', 'birthdate']
    model = 'res.users'

    def read(self):
        result = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'read', [self.uid], self.columns)
        return result


class Address(BaseModel):
    columns = ['name', 'street', 'city', 'zip', 'phone', 'mobile', 'email', 'type', 'active']
    model = 'res.partner'

    def create(self, name, street, city, zip, phone, mobile, email, user_id, add_type='contact', active=True):
        '''
        @:param name str；
        @:param street str；
        @:param city str;
        @:param zip str;
        @:param phone str;
        @:param mobile str;
        @:param email str;
        @:param add_type str['contact'];
        @:param active boolean;
        '''
        objid = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'create',
                            {'name': name, 'street': street, 'city': city, 'zip': zip, 'phone': phone, 'mobile': mobile,
                             'email': email, 'user_id': user_id, 'type': add_type, 'active': active})
        return objid

    def search(self, domain):
        '''
        @:param domain list [('user_id','=',1)]
        '''
        objids = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'search', domain)
        return objids

    def unlink(self, ids):
        '''
        @:param ids int list [1,2,3]
        '''
        flag = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'unlink', ids)
        return flag

    def read(self, ids):
        '''
        @:param ids int list [1,2,3]
        '''
        addresses = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'read', ids, self.columns)
        return addresses


class Category(BaseModel):
    columns = []
    model = 'product.category'

    def search(self, domain):
        objids = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'search', domain)
        return objids

    def read(self, ids):
        '''
        @:param ids int list [1,2,3]
        '''
        addresses = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'read', ids, self.columns)
        return addresses


class Product(BaseModel):
    columns = []
    model = 'product.template'

    def search(self, domain):
        objids = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'search', domain)
        return objids

    def read(self, ids):
        '''
        @:param ids int list [1,2,3]
        '''
        addresses = OBJ.execute(DB, admin_uid, admin_pwd, self.model, 'read', ids, self.columns)
        return addresses

    def share(self):
        pass


class SaleOrder(BaseModel):
    columns = []
    model = 'sale.order'

    def search(self):
        pass

    def unlink(self):
        pass

    def add_to_cart(self):
        pass

    def delete_from_cart(self):
        pass

    def update_cart_quantity(self):
        pass

    def comfirm_order(self):
        pass

    def get_paylink(self):
        pass

    def check_state(self):
        pass
