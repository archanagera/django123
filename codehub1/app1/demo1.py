import datetime as dt

import pytz

d=dt.datetime.now()

d1=d.astimezone(pytz.utc)
print(d1)