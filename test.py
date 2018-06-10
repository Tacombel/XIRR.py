import datetime
import XIRR

values = [-18990, -23320, 49490]
dates = [datetime.date(2016, 2, 5), datetime.date(2018, 1, 26), datetime.date(2018, 6, 5)]

print(XIRR.xirr(values, dates))
