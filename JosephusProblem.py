# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:57:33 2024

@author: Vaishali
"""



def jo(n,k):
    if n==1:
        return 1
    else:
        return (jo(n-1,k)+k-1)%n+1
    
n=5
k=3
result=jo(n,k)
print("result is ",result)