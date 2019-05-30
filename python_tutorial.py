# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:16:35 2019

@author: kanis
"""
## HOW TO USE MAP 
#map(function_to_apply, list_of_inputs)
def multiply(x):
    return x*x 

def add(x):
    return x+x 

print(list(map(multiply, [1,2,3])))   # USING WITHOUT LAMBDA
print(list(map(lambda x : x*2, range(10))))  # using with LAMBDA
print(list(map(multiply, range(5))))  
print(list(map(add, range(5))))
#print(list(map(multiply,add,  range(5))))   can't put two functions at same place 

