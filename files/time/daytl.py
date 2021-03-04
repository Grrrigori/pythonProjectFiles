# import datetime
# # twentyfour_hours = twentyfour_hours.hour
#
# dt_now = datetime.datetime.now()
#
# print(dt_now)
import time
# now = time.gmtime()
# print(now[0])  # Will print tm_year
#
# print(now[3:5])

now2 = time.asctime()  # Prints time in more suitable format
print(now2)

stop = time.time()
start =time.time()
print(stop - start)