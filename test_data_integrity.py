
from validators import find_dupes, is_valid_date, is_valid_email, missing_reference
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
        bad_rows = is_valid_date(users, 'signup_date')
        assert not bad_rows, f"Users with malformed signup_date: {bad_rows}"

    @pytest.mark.users
    def test_valid_emails(self, users):
        bad_rows = [row["email"] for row in users if not is_valid_email(row["email"])]
        assert not bad_rows, f"Invalid emails: {bad_rows}"

    @pytest.mark.orders
    def test_order_dates(self, orders):
        bad_rows = is_valid_date(orders, 'order_date')
        assert not bad_rows, f"Orders with malfornmed signup date: {bad_rows}"

class TestBusinessRules:

    @pytest.mark.orders
    def test_no_negative_order_amounts(self, orders):
        negative = [order for order in orders if order['amount'] < 0]
        assert not negative, f"Orders with negative amount: {negative}"

    @pytest.mark.orders
    def test_order_status_is_known_value(self, orders):
        allowed = {"completed", "refunded", "cancelled", "pending"}
        status = [row["status"] for row in orders if row["status"] not in allowed]
        assert not status, f"Status not allowed {status}"

    @pytest.mark.slow
    def test_all_orders_reference_existing_users(self, users, orders):
        known_user_ids = [row["user_id"] for row in users]
        order_user_ids = [str(order["user_id"]) for order in orders]
        missing_user_id = missing_reference(order_user_ids, known_user_ids)
        assert not missing_user_id, f"Orders reference user_id(s) that don't exist in users.csv: {missing_user_id}"
