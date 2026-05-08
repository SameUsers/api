from datetime import datetime, timezone


def get_time():
    return datetime.now(tz=timezone.utc)