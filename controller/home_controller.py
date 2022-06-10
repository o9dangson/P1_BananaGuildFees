from flask import redirect, session, render_template, url_for
from service.logger_service import log_get_req

def get_homepage():
    if check_not_in_session():
        log_get_req('/', "render_template('index.html')")
        return render_template('index.html')
    else:
        log_get_req('/', "redirect('/account')")
        return redirect(url_for("account"))

def get_homepage_err():
    if check_not_in_session():
        log_get_req('/error', "render_template('index.html', err=True)")
        return render_template('index.html', err=True)
    else:
        log_get_req('/', "redirect('/account')")
        return redirect(url_for("account"))

    
def check_not_in_session():
    return not 'user_id' in session