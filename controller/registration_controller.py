from flask import request, render_template, redirect

def get_register_page():
    log_get_req('/register', "render_template('register.html', error=None)")
    return render_template('register.html', error=None)

    
def get_register_err():
    log_get_req('/register/error', "render_template('register.html', error='POST')")
    return render_template('register.html', error='POST')

def is_valid_in_database(input):
    if 'username' in input and 'password' in input:
        user = input.get('username')
        pw = input.get('password')
        login_obj = select_login_by_user(user)
        if login_obj is None:
            return True
    return False

def valid_input(input):
    if 'username' in input and 'password' in input:
        user = input.get('username')
        pw = input.get('password')
        if len(user) >= 1 and len(user) <=50 and len(pw) >= 1 and len(pw) <=50:
            return True
    print( f"user: {len(user)}\t pw: {len(pw)}")
    return False

def add_account(input):
    user = input.get('username')
    pw = input.get('password')
    f_name = input.get('f_name')
    l_name = input.get('l_name')
    #insert_login(user, pw)
    #user_login = select_login(user, pw)
    #insert_user(user_login.user_id, user_login.user_id, f_name, l_name)

def attempt_registration(input):
    if valid_input(input) and is_valid_in_database(input):
        #add_account(input)
        #log_post_req('/register/input', "redirect('/')")
        return redirect('/')
    else:
        #log_post_req('/register/input', "redirect('/register/error')")
        return redirect('/register/error')