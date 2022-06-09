from flask import Flask, render_template, request
from service.logger_service import setup_logger_obj
from service.account_service import verify_details

def get_account_page(form):
    # Verify details
    # get user id by login function
    user_id = verify_details(form.get('username'), form.get('password'))
    if user_id != 0:
        # Log
        # Render account.html
        pass
    else:
        # Log
        # return error, let js file update html
        pass