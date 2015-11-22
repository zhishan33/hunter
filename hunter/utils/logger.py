# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from hunter.view import app
import traceback
import sys


class PrintLog(object):
    def __init__(self):
        pass

    @classmethod
    def get_sys_info(cls):
        etype, values, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        co = f.f_code
        filename = co.co_filename
        name = co.co_name
        detail = 'File "%s", line %d, in %s' % (filename, lineno, name)
        s = traceback.format_exception_only(etype, values)
        etype = values = tb = None
        return detail + ' message: ' + ','.join(s)

    # 无异常log
    @classmethod
    def print_log(cls, *args, **kwargs):
        params = ''
        for key, value in kwargs.items():
            params += key + ':' + str(value) + ' '
        app.logger.info('error_no_exception ' + params)

    # 普通错误日志
    @classmethod
    def print_normal_log(cls, *args, **kwargs):
        e_detail = cls.get_sys_info()
        params = ''
        for key, value in kwargs.items():
            params += key + ':' + str(value) + ' '
        app.logger.error(e_detail + ' normal_error ' + params)
