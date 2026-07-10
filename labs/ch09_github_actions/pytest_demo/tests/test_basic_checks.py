from labs.ch09_github_actions.pytest_demo.src.basic_checks import is_valid_order_status

def test_valid_order_status():
    assert is_valid_order_status("DELIVERED") is True

def test_invalid_order_status():
    assert is_valid_order_status("UNKNOWN") is False
