from flask import render_template, session, redirect, url_for
from service.logger_service import log_get_req, log_post_req

def get_manage_page(form=None):
    if 'user_id' in session and 'is_manager' in session:
        if form is None:
            log_get_req('/account/manage', "render_template('manage.html', manager=session['is_manager'])")
            return render_template('manage.html', manager=session['is_manager'])
        else:
            # Post version, no rendering, just updating db
            return render_template('manage.html', manager=session['is_manager'])
    else:
        if form is None:
            log_get_req('/account/manage', "redirect(url_for('account'))")
        else:
            log_post_req('/account/manage', "redirect(url_for('account'))")
        return redirect(url_for('account'))