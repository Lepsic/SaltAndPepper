import datetime


def date_in_feature(days: int) -> datetime:
    current_date = datetime.datetime.now()
    day = datetime.timedelta(days=days)
    current_date = current_date + day
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

