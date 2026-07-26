# pytest data validation

Small pytest suite that checks the sample `users.csv` and `orders.json` files for data quality issues - dupes, bad formats, invalid business rules, orphaned references, that kind of thing.

## Layout

- `data/users.csv` and `data/orders.json` - the data being checked
- `conftest.py` - loads the data into fixtures
- `validators.py` - the actual checks (dupes, date format, email format, missing references)
- `test_data_integrity.py` - the tests, grouped by what they check

## Running

```
pytest
```

Only run one dataset's tests:

```
pytest -m users
pytest -m orders
```

Skip the slow ones:

```
pytest -m "not slow"
```

## What's checked

- Files load and aren't empty
- No duplicate `order_id` / `user_id`
- `signup_date` and `order_date` are `YYYY-MM-DD`
- Emails look valid
- Order amounts aren't negative
- Order `status` is one of `completed`, `refunded`, `cancelled`, `pending`
- Every order's `user_id` exists in `users.csv`
