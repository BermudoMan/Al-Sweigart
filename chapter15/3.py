import datetime, time

print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(halloween2015 == oct31_2015)
print(halloween2015 > oct31_2015)


delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))


dt = datetime.datetime.now()
print(dt)
thousands_days = datetime.timedelta(days=1000)
print(dt + thousands_days)