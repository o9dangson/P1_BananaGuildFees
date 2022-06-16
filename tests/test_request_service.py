import json
import pytest

from service.request_service import get_all_pending_requests, update_request_status

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