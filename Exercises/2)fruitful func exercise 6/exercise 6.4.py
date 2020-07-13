# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:40:44 2020

@author: MehmetZahit
"""
#%% Chapter 6 . Example 4-5

def day_name(day):
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "sunday"
    else:
        return "Please enter a number between 0-6"



def day_num(num):
     if num == "monday":
         return 0
     elif num == "tuesday":
         return 1
     elif num == "wednesday":
         return 2
     elif num == "thursday":
         return 3
     elif num == "friday":
         return 4
     elif num == "saturday":
         return 5
     elif num == "sunday":
         return 6
     else:
         return "Please write a day "

dayn = input("Please enter a day name ").lower()

i = int(input("add"))
a = int((day_num(dayn)+ i) % 7)
print(day_name(a))
