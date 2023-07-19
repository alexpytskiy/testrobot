from datetime import datetime as dt
from datetime import timedelta

date = dt.now() + timedelta(days = -3)
date_2 = date.strftime('%Y-%m-%d')


