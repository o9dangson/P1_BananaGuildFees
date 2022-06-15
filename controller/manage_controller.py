from flask import render_template, session, redirect, url_for
from service.logger_service import log_get_req, log_post_req
from service.request_service import get_all_pending_requests, update_request_status

def get_manage_page(request):
    if 'user_id' in session and 'is_manager' in session:
        if request.method == 'GET':
            log_get_req('/account/manage', "render_template('manage.html', manager=session['is_manager'])")
            return render_template('manage.html', manager=session['is_manager'])
        else:
            log_post_req('/account/manage', 'redirect(url_for("account"))')
            return redirect(url_for("account"))
    else:
        log_get_req('/account/manage', "redirect(url_for('account'))")
        return redirect(url_for('account'))


def get_manage_requests(request):
    if 'user_id' in session:  
        if request.method == "GET" and session['is_manager']:
            return get_all_pending_requests(session['user_id'])
        else:
            return redirect(url_for('account'))
    else:
        return redirect(url_for('home'))

def post_manage_update(request):
    if 'user_id' in session:  
        if request.method == "POST" and session['is_manager']:
            jsonData = request.get_json()
            return update_request_status(jsonData.get('req_id'), jsonData.get('status'))               
        else:
            return redirect(url_for('account'))
    else:
        return redirect(url_for('home'))