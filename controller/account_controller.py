from flask import Flask, render_template, request, session
from service.logger_service import log_get_req, log_post_req, setup_logger_obj
from service.account_service import verify_details

def get_account_page(form):
    # Verify details
    # get user id by login function
    user_id = verify_details(form.get('username'), form.get('password'))
    return render_template('index.html', err=True)
    if user_id != 0:
        # Set session details
        session['user_id'] = user_id
        log_post_req('/account', render_template("account.html"))
        return render_template("account.html")
    else:
        print("user does not exist")
        log_post_req('/account', "render_template('index.html', err=True)")
        return render_template('index.html', err=True)