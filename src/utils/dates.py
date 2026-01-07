import random
from datetime import datetime, timedelta

def random_past_datetime(days=365):
    return datetime.now() - timedelta(days=random.randint(1, days))

def random_future_date(days=90):
    return datetime.now().date() + timedelta(days=random.randint(1, days))

def avoid_weekends(date):
    while date.weekday() >= 5:
        date += timedelta(days=1)
    return date