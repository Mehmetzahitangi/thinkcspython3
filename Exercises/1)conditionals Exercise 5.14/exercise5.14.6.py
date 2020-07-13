# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:48:07 2020

@author: MehmetZahit
"""
#%%
def exam_grades(inp):    
    for i in inp:
        if i >= 75 and i <= 100:
            print("First")
        elif i < 75 and i >= 70:
            print("Upper Second")
        elif i < 70 and i >= 60:
            print("Second")
        elif i < 60 and i >= 50:    
            print("Third")
        elif i < 50 and i >= 45:
            print("F1 supp")
        elif i < 45 and i >= 40:
            print("F2")
        elif i<40 and i >=0:
            print("F3")
        else:
            print("Grade must be betwen 0-100.")
              
grade = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
exam_grades(grade)           
