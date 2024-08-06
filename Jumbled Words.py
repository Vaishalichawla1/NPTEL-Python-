# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

def choose():
    words=['beach','cake','chocolate','samosa','umbrella','kulfi','contemplate','comprehend','rapport','cohesive','croissant','compliment']
    c=random.choice(words)
    return c

def jumble(word):
    jumbled= "".join(random.sample(word,len(word)))
    return jumbled


def thank(p1n,p2n,ps1,ps2):
    print(p1n,' ,Your score is ',ps1)
    print(p2n,' ,Your score is ',ps2)
    print('Thanks for playing!')
    
def play():
    p1= input('Player1, Enter your name: ')
    p2= input('Player2, Enter your name: ')
    pp1= 0
    pp2= 0
    turn=0
    
    while(1):
        pick=choose()
        qn=jumble(pick)
        print (qn)
        
        #Player 1
        if turn%2==0:
            print(p1,', your turn!',end='\n')
            ans= input('Guess what is on my mind...')
            if ans==pick:
                pp1=pp1+1 
                print('Yayyy!! Correct answer. Your score is :',pp1,end='\n')
            else:
                print('Wrong answer!! Better luck next time.',end='\n')
            choice=int(input('Enter 1 if you want to continue and 0 if you want to quit:'))
            
            if choice==0:
                thank(p1,p2,pp1,pp2)
                break
        # Player 2
        else:
                print(p2,', your turn!',end='\n')
                ans= input('Guess what is on my mind...')
                if ans==pick:
                    pp2=pp2+1 
                    print('Yayyy!! Correct answer. Your score is :',pp2,end='\n')
                else:
                    print('Wrong answer!! Better luck next time.',end='\n')
                choice=int(input('Enter 1 if you want to continue and 0 if you want to quit:'))
                
                if choice==0:
                    thank(p1,p2,pp1,pp2)
                    break
        turn=turn+1
            
play()