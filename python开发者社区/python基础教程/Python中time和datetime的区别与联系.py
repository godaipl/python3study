import time
import datetime

print(time.time())
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S'))

time_now = datetime.datetime.now()
print(time_now)
print(time_now.strftime('%Y-%m-%d %H:%M:%S'))
delta = datetime.timedelta(hours=24)
print(time_now + delta)
print(time_now - delta)
