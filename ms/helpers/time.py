import pytz
from datetime import (
    date as datetime_instance,
    datetime)
from ms import app


app_tz = app.config.get('TIMEZONE')


def now(tz=app_tz):
    return datetime.now(tz=pytz.timezone(tz))


def datetime_to_epoch(date):
    if isinstance(date, datetime_instance):
        date = datetime.combine(date, datetime.min.time())
    return int(date.timestamp())


def epoch_now():
    return datetime_to_epoch(now())
