from database.login_dao import select_user_by_login
from database.user_info_dao import select_user_info_by_user_id

def verify_details(username, password):
    return select_user_by_login(username, password)

def check_account_type(user_id):
    user_info_object = select_user_info_by_user_id(user_id)
    if user_info_object.role == 'gm':
        return True
    elif user_info_object.role == 'adv':
        return False
        