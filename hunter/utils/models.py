# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import xmlrpclib
from hunter.config.setting import common
from hunter.view import session


class BaseModel(object):
    def __init__(self, db, username, userpwd, model):
        self.db = db
        self.username = username
        self.userpwd = userpwd
        self.model = model
        self.login()

    def login(self):
        uid = common.login(self.db, self.username, self.userpwd)
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
