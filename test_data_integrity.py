
from validators import find_dupes, is_valid_date, is_valid_email
import pytest

@pytest.mark.orders
def test_can_load_orders(orders):
    assert len(orders) > 0

@pytest.mark.users
def test_can_load_users(users):
    assert len(users) > 0

@pytest.mark.orders
def test_no_duplicate_order_ids(orders):
    ids = [row["order_id"] for row in orders]
    dupes = find_dupes(ids)
    assert not dupes, f"Duplicate order_id value found: {dupes}"

@pytest.mark.users
def test_no_duplicate_user_ids(users):
    ids = [row["user_id"] for row in users]
    dupes = find_dupes(ids)
    assert not dupes, f"Duplicate user_id values found: {dupes}"

@pytest.mark.users
def test_signup_dates_valid_format(users):
    bad_rows = is_valid_date(users)
    assert not bad_rows, f"Users with malformed signup_date: {bad_rows}"

@pytest.mark.users
@pytest.mark.parametrize("row_index", range(1))
def test_valid_emails(users, row_index):
    row = users[row_index]
    assert is_valid_email(row["email"]), f"invalid email {row['email']}"