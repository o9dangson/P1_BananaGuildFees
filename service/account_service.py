from database.login_dao import select_user_by_login

def verify_details(username, password):
    print(f"{username}\t{password}")
    return select_user_by_login(username, password)