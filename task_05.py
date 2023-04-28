import datetime


def date_in_future(days) -> datetime:
    if type(days) != int:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_date = datetime.datetime.now()
    day = datetime.timedelta(days=days)
    current_date = current_date + day
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

