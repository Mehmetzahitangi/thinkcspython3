# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:35:45 2020

@author: MehmetZahit
"""
#%%
sleeps = 137
finish_day = 137 % 7
# wednesday is third day
day = int(3+ finish_day)
if day == 1:
    print("{}th day is Monday as finish day".format(day))
elif day == 2:
    print("{}th day is Tuesday as finish day".format(day))
elif day == 3:
    print("{}th day is Wednesday as finish day".format(day))
elif day == 4:
    print("{}th day is Thursday as finish day".format(day))
elif day == 5:
    print("{}th day is Friday as finish day".format(day))
elif day == 6:
    print("{}th day is Saturday as finish day".format(day))
elif day == 7:
    print("{}th day is Sunday as finish day".format(day))