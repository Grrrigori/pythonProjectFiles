stop_light = int(input("Please insert any number to star:"))
# while True:
#     if stop_light <10:
#         print ("Green")
#         stop_light += 1
#     elif stop_light <20:
#         print ("Yellow")
#         stop_light +=1
#     elif stop_light <30:
#         print ("Red")
#         stop_light += 1
#     elif stop_light >= 30:
#         stop_light = 0

import datetime
day= datetime.timedelta( hours=[1:12])
while True:
    if stop_light < 10:
        print('Green')
        stop_light += 1

    elif stop_light < 15:
        print('Green blinks')
        stop_light +=1
    elif stop_light < 20:
        print('Yellow')
        stop_light +=1
    elif stop_light < 25:
        print('Yellow blinks')
        stop_light +=1
    elif stop_light < 30:
        print('Red')
        stop_light += 1
    elif stop_light >= 30:
        # print('Yelow blinks(night regime)')
        stop_light = 0


