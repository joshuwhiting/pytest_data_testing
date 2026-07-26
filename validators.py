from datetime import datetime
from collections import Counter

def find_dupes(values):
    dupes = Counter(values)
    return [item for item, dupe in dupes.items() if dupe > 1]

def is_valid_email(emails):
    if not isinstance(emails, str):
        return False
    if emails.count('@') != 1:
        return False
    local, _, domain = emails.partition("@")
    return bool(local) and "." in domain

def is_valid_date(rows,row_name):
    bad_rows = []
    for row in rows:
        try:
            datetime.strptime(row[row_name], "%Y-%m-%d")
        except ValueError as e:
            bad_rows.append(row)
    return bad_rows

def missing_reference(child_value, parent_value):
    parent_set = set(parent_value)
    return sorted({value for value in child_value if value not in parent_set})