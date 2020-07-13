# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:07:13 2020

@author: MehmetZahit
"""
#%%


x = int(input("Please enter x lenght "))
y = int(input("Please enter y lenght "))
if x > 0 and y > 0:
    hypotenuse = ((x**2)+(y**2))**0.5
    print(hypotenuse)
else:
    print("x and y must be greater than 0") 
