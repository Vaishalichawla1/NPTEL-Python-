# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:05:53 2024

@author: Vaishali
"""

def FizzBuzz(n):
    for i in range(1,n):
        print(i,end=" ")
        if(i%3==0 and i%5==0):
            print(" FizzBuzz")
        else:
            if(i%3==0):
                print(" Fizz")
            else:
                if(i%5==0):
                    print(" Buzz")
                else:
                    print(end="\n")
                    
n=(int)(input("Enter the limit : "))
FizzBuzz(n) 