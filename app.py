import re
from flask import Flask, render_template, request, redirect, session, url_for
from service.logger_service import setup_logger_obj
from controller.home_controller import get_homepage, get_homepage_err
from controller.account_controller import get_account_page
from controller.manage_controller import get_manage_page
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
            return redirect(url_for('home'))

    @app.route('/account/manage', methods=['GET', 'POST'])
    def manage():
        if request.method=='GET':
            return get_manage_page()
        elif request.method=='POST':
            return get_manage_page(request.form)
        
    @app.route('/logout', methods=["GET"])
    def logout():
        if request.method=='GET':
            session.pop('user_id', None)

        return redirect(url_for("home"))
        
        
    #@app.route('/register', methods=['GET'])
    #def register():
    #    return get_register_page()
    #
    #@app.route('/register/input', methods=['POST'])
    #def register_input():
    #    return attempt_registration(request.form)
    #
    #@app.route('/register/error', methods=['GET'])
    #def register_err():
    #    return get_register_err()
    

if __name__ == '__main__':
    setup_logger_obj()
    App.app.run(debug=True)
   