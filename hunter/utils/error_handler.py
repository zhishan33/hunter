# -*- coding: utf-8 -*-
__author__ = 'canhuayin@gmail.com'
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from hunter.view import app, render_template


@app.errorhandler(404)
def error_404():
    return render_template('hunter_error_40x.html.html', {}), 404


@app.errorhandler(500)
def error_500():
    return render_template('hunter_error_50x.html.html', {}), 500
