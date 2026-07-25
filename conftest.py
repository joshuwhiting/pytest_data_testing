import pytest
import csv
import json

@pytest.fixture
def users():
    with open("data/users.csv", newline="") as f:
        return list(csv.DictReader(f))

@pytest.fixture
def orders():
    with open("data/orders.json") as f:
        return json.load(f)