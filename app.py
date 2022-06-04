from flask import Flask, render_template, request


class App:
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')
    
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
    App.app.run(debug=True)