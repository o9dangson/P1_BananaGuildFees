from flask import Flask, render_template, session, redirect, url_for
from service.logger_service import log_post_req
from service.account_service import check_account_type, verify_details

def get_account_page(form):
    # Verify details
    # get user id by login function
    user_id = verify_details(form.get('username'), form.get('password'))
    if user_id != 0:
        # Set session details
        session['user_id'] = user_id
        if ('user_id' in session):
            return render_page()
        else:
            log_post_req('/account', 'render_template("index.html")')
            return redirect(url_for("home"))  
    else:
        log_post_req('/account', "redirect('/error')")
        return redirect('/error')

def get_logged_in_account_page():
    if 'user_id' in session:
        return render_page()
    else:
        return redirect(url_for('home'))

def render_page():
    log_post_req('/account', "render_template('account.html', manager=session['is_manager']")
    session['is_manager'] = check_account_type(session['user_id'])
    return render_template("account.html", manager=session['is_manager'])