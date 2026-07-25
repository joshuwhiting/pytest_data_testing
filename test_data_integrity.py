
from validators import find_dupes, is_valid_date, is_valid_email
import pytest

class TestFiles:
    @pytest.mark.orders
    def test_can_load_orders(self, orders):
        assert len(orders) > 0

    @pytest.mark.users
    def test_can_load_users(self, users):
        assert len(users) > 0



class TestDuplicates:
    @pytest.mark.orders
    def test_no_duplicate_order_ids(self, orders):
        ids = [row["order_id"] for row in orders]
        dupes = find_dupes(ids)
        assert not dupes, f"Duplicate order_id value found: {dupes}"

    @pytest.mark.users
    def test_no_duplicate_user_ids(self, users):
        ids = [row["user_id"] for row in users]
        dupes = find_dupes(ids)
        assert not dupes, f"Duplicate user_id values found: {dupes}"


class TestValidFormats:
    @pytest.mark.users
    def test_signup_dates_valid_format(self, users):
        bad_rows = is_valid_date(users)
        assert not bad_rows, f"Users with malformed signup_date: {bad_rows}"

    @pytest.mark.users
    def test_valid_emails(self, users):
        bad = [row["email"] for row in users if not is_valid_email(row["email"])]
        assert not bad, f"Invalid emails: {bad}"

    
