# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:57:39 2022

@author: kacpe
"""



'zad1'
'''  
def func(names):
    for name in names:
        print(name)
names=['tomek', 'kacper', 'szymon', 'wojtek', 'bartel']

func(names)

'''
'''
def x2(numbers):
    res = []
    for number in numbers:
        res.append(number * 2)
    return res

numbers = [2, 8, 12, 18, 123]

x2(numbers)
'''


'''
def x2(numbers):
    return [number * 2 for number in numbers]

numbers = [2, 8, 12, 18, 123]

x2(numbers)
'''


'''
def even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)
            
numbers = [16, 27, 9, 90, 6, 102, 19, 22, 45, 88]

even(numbers)
'''





'''
def func(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])
        
numbers = [16, 27, 9, 90, 6, 102, 19, 22, 45, 88]

func(numbers)

'''














