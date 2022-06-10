from flask import Flask, render_template, session, redirect, url_for
from service.logger_service import log_post_req
from service.account_service import verify_details

def get_account_page(form):
    # Verify details
    # get user id by login function
    user_id = verify_details(form.get('username'), form.get('password'))
    if user_id != 0:
        # Set session details
        session['user_id'] = user_id
        if ('user_id' in session):
            log_post_req('/account', render_template("account.html"))
            # Check if user is manager or not
            return render_template("account.html")
        else:
            log_post_req('/account', render_template("index.html"))
            return redirect(url_for("home"))  
    else:
        log_post_req('/account', "redirect('/error')")
        return redirect('/error')

