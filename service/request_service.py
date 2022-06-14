from database.request_dao import insert_user_request, select_all_req_by_user_id, select_all_req_by_manager_id, update_req_by_req_id, remove_req_by_req_id
import json

def get_all_pending_requests(user_id):
    list_of_req_obj = select_all_req_by_manager_id(user_id)
    json_list = []
    for obj in list_of_req_obj:
        json_list.append(obj.to_dict())
    return json.dumps({'json_list': json_list})

# status = "Accepted" or "Rejected"
# Returns True if successful, else False
def update_request_status(request_id, status):
    attempt_update = update_req_by_req_id(int(request_id), 'status', status)
    my_dict = create_dict('attempt_update', attempt_update)
    return json.dumps(my_dict)

# Returns True if successful, else False
def cancel_pending_request(request_id):
    attempt_cancel = remove_req_by_req_id(request_id)
    my_dict = create_dict('attempt_cancel', attempt_cancel)
    return json.dumps(my_dict)


def get_user_requests(user_id):
    list_of_req_obj = select_all_req_by_user_id(user_id)
    json_list = []
    for obj in list_of_req_obj:
        json_list.append(obj.to_dict())
    return json.dumps({'json_list': json_list})

# Returns id of inserted request
def create_user_request(user_id, amount, desc):
    new_req_id = insert_user_request(user_id, amount, desc)
    my_dict = create_dict('new_req_id', new_req_id)
    return json.dumps(my_dict)

def create_dict(varName, var):
    return { varName: var}