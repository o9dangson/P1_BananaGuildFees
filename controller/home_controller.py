from flask import request, render_template
from service.logger_service import log_get_req

def get_homepage():
    log_get_req('/', "render_template('index.html')")
    return render_template('index.html')

def get_homepage_err():
    log_get_req('/error', "render_template('index.html', err=True)")
    return render_template('index.html', err=True)
    
