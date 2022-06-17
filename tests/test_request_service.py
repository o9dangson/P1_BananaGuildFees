import json
import pytest
from database.request_dao import insert_user_request

from service.request_service import cancel_pending_request, get_all_pending_requests, update_request_status

@pytest.mark.parametrize("user_id, expected", [
    (1, True), (99, True) 
])
def test_pending_request_returns_json(user_id, expected):
    json_pending = get_all_pending_requests(user_id)

    try:
        json.loads(json_pending)
        ans = True
        assert ans == expected
    except ValueError as err:
        ans = False
        assert ans == expected

@pytest.mark.parametrize("req_id, status, expected", [
    (2, 'Pending', True), (10000, 'Pending', False) 
])
def test_pending_request_returns_json(req_id, status, expected):
    json_pending = update_request_status(req_id, status)

    try:
        val = json.loads(json_pending)
        assert val.get('attempt_update') == expected
    except ValueError as err:
        assert True

@pytest.mark.parametrize("is_new_req, expected", [
    (True, True), (False, True)
])
def test_cancel_request_returns_json(is_new_req, expected):
    req_id = 0
    if is_new_req:
        req_id = insert_user_request(2, 500, "Default Description")
    json_pending = cancel_pending_request(req_id)
    try:
        val = json.loads(json_pending)
        assert val.get('attempt_cancel') == expected
    except ValueError as err:
        assert True