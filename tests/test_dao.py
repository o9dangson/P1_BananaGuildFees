import pytest
from database.login_dao import select_user_by_login
from database.request_dao import *

from database.user_info_dao import select_user_info_by_user_id

#Requests
# TC_08
def test_select_req_dao():
    list_of_req = select_all_req_by_user_id(1)
    assert list_of_req is not None
    #for req in list_of_req:
        #print(f"{req.req_id}\t{req.user_id}\t{req.amount}\t{req.desc}\t{req.status}")
    #assert True == False


    test = select_all_req_by_manager_id(2)
    assert test is not None
    #for req in test:
    #    print(f"{req.req_id}\t{req.user_id}\t{req.amount}\t{req.desc}\t{req.status}")
    #assert True == False

# TC_05
@pytest.mark.parametrize("test", [
    {'u_id': 1, 'amt': 250, 'desc': 'Default_desc', 'status':'Accepted'},
    {'u_id': 2, 'amt': 300, 'desc': 'Def_man_desc', 'status': 'Rejected'}
])
def test_insert_update_delete_req_dao(test):
    req_id = insert_user_request(test['u_id'], test['amt'], test['desc'])
    assert req_id != 0
    up_qry = update_req_by_req_id(req_id, 'status', test['status'])
    assert up_qry == True
    del_qry = remove_req_by_req_id(req_id)
    assert del_qry == True

#Users
# TC_01
@pytest.mark.parametrize("test, expected", [
    (['employee', 'Password123'], 1), (['yo', 'thisisapassword'], 0), (['ManaGER', 'P1223'], 0)
])
def test_user_login(test, expected):
    user_id = select_user_by_login(test[0], test[1])
    assert user_id == expected

@pytest.mark.parametrize("test, expected", [
    ({'u_id': 1}, {'f_name': 'Ground', 'l_name': 'Last', 'role': 'adv'}),
    ({'u_id': 3}, None)
])
def test_user_info(test, expected):
    user_info_obj = select_user_info_by_user_id(test['u_id'])
    if expected is not None:
        assert user_info_obj is not None
    else:
        assert user_info_obj is None
    if user_info_obj is not None:
        assert user_info_obj.first_name == expected['f_name']
        assert user_info_obj.last_name == expected['l_name']
        assert user_info_obj.role == expected['role']