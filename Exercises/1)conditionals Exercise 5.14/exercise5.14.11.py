# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:17:33 2020

@author: MehmetZahit
"""
#%%
def is_rightangled():
    a = int(input("Please enter one short side of short sides "))
    b = int(input("Please enter other short side "))
    c = int(input("Please enter long side(hypotenuse) "))
    if ((a**2) + (b**2) == (c**2)):
        return True
    else:
        return False

is_rightangled()      