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

def is_valid_date(rows):
    bad_rows = []
    for row in rows:
        try:
            datetime.strptime(row["signup_date"], "%Y-%m-%d")
        except ValueError as e:
            bad_rows.append(row)
    return bad_rows

