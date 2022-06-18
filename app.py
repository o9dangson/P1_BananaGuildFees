import re
from flask import Flask, request
from service.logger_service import setup_logger_obj
from controller.home_controller import get_homepage, get_homepage_err, get_logout_page
from controller.account_controller import get_account_page, get_logged_in_account_page, get_user_requests_list, post_cancel_request, post_create_request
from controller.manage_controller import get_manage_page, get_manage_requests, post_manage_update
import secrets


class App:
    app = Flask(__name__)
    app.secret_key = secrets.token_hex()

    @app.route('/', methods=['GET'])
    def home():
        return get_homepage()

    @app.route('/error', methods=['GET'])
    def home_error():
        return get_homepage_err()

    @app.route('/account', methods=['GET', 'POST'])
    def account():
        if request.method=='POST':
            return get_account_page(request.form)
        elif request.method=='GET':
            return get_logged_in_account_page()

    @app.route('/account/request', methods=['GET'])
    def request():
        return get_user_requests_list()

    @app.route('/account/cancel', methods=['POST'])
    def cancel_request():
        return post_cancel_request(request)

    @app.route('/account/create', methods=['POST'])
    def create_request():
        return post_create_request(request)

    @app.route('/account/manage', methods=['GET'])
    def manage():
        return get_manage_page(request)
        
    @app.route('/logout', methods=["GET"])
    def logout():
        return get_logout_page(request)
        
    @app.route('/manage/all-requests', methods=['GET'])
    def list_requests_manage():
        return get_manage_requests(request)

    @app.route('/manage/request-update', methods=["POST"])
    def update_requests_manage():
        return post_manage_update(request)
    

if __name__ == '__main__':
    setup_logger_obj()
    App.app.run(debug=True)
   