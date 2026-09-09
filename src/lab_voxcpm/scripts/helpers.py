import datetime as dt

def _log_now():
    _now =  dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M:%S")
    return _now