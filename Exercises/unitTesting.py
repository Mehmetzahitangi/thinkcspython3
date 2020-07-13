# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:50:59 2020

@author: MehmetZahit
"""
#%% A BASIC TEST CODE
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

dayy = int(input("enter a day as a number "))
print("The number of days starts zero.",day_name(dayy))

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
print(day_num(dayn))



import sys
def test(did_pass):
    # """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    
    print(msg)

def test_suite():
   # """ Run the suite of tests for code in this module (this file)."""
    test(day_num("sunday") == 3)
    test(day_name(5) == "Saturday")

test_suite()