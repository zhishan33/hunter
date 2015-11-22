# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from logging import FileHandler
from hunter import app
app.secret_key = '\xbbU\x90CQ\xba\r\x83\xa9\x94\xb773\xa2)\xc7\xdd%\x8d\xbdeCT\xf8'
app.debug = True
if not app.debug:
    import logging
    file_handler = FileHandler('log/serverlog')
    file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
