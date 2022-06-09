from flask import Flask, render_template, request, redirect, url_for
from service.logger_service import setup_logger_obj
from controller.account_controller import get_account_page


class App:
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    @app.route('/account', methods=['GET', 'POST'])
    def account():
        if request.method=='POST':
            return get_account_page(request.form)
        else:
            redirect(url_for('home'))

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
   