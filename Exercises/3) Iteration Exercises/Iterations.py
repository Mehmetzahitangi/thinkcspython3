# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:56:37 2020

@author: MehmetZahit
"""
#%%
# Test codes were not write
func = (3,2,4,5,6,8,-2,11111)

def odd_num_count(n):
    count = 0
    for i in n:
        if (i % 2 != 0):
            count += 1
        else:
            continue
    print(count)
odd_num_count(func)

def sum_even_num(n):
    sumNumber = 0
    for i in n:
        if (i % 2 == 0):
            sumNumber += i
        else:
            continue
    print(sumNumber)
sum_even_num(func)

def sum_negative_num(n):
    sumNumber = 0
    for i in n:
        if (i < 0):
            sumNumber += i
        else:
            continue
    print(sumNumber)
sum_negative_num(func)

a = str(func) # bu şekilde yapınca boyutu 1 olan bir string oluyor ********************************
strN = ("11111","cc","ddx","ggr") # bu şekilde ise boyutu 4 olan bir tuple ***************************
def five_lenght_words(n):
    count = 0
    for i in n:
        if (len(i)==5):
            count += 1
        else:
            continue
    print(count)
    
five_lenght_words(strN)


def sum_num(num_list): # Important exercise
    total = 0
    once = False
    for i in num_list:
        if ((i % 2 == 0) and  (once  == False)):  #  or we can write like "if i % 2 == 0 and not once:"  **************
            once = True
            continue
        total += i
    print(total)

sum_num(func)

# ******************** form tuple to list and splitting***************
strN = ("11111","cc","ddx","ggr","samm uncle","samurai")
def five_lenght_words(n):
    count = 0
    splits = list(n)
    for i in splits:
        if (i[0] == "s" and i[1] == "a" and i[2] == "m" ):
            count += 1
    print(count) 
five_lenght_words(strN)


def print_triangular_numbers(n):
    for i in range(1,n+1):
        print(i,"\t",int((i*(i+1))/2))
        
print_triangular_numbers(10)

