# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 03:54:46 2024

@author: Vaishali
"""

import string
import random

symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)

if(pos1==pos2):
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
    
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i+=1

print("Card I: ",end=" ")
print(card1)
print("Card II: ",end=" ")
print(card2)

ans=input("Spot the same symbol: ")
if(ans==samesymbol):
    print("You are correct!")
else:
    print("That is incorrect!")
        
    