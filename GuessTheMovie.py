# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:12:08 2024

@author: Vaishali
"""

import random
movies=['munjya', 'singham', 'dil dhadakne do', 'jatt and julliet', 'teri baaton mein esa uljha jiya', 'jajantram mamantram', 'vivaah', 'crew', 'good newz', 'bad newz', 'kudi haryane val di']


def thank(p1name,p2name,pp1,pp2):
    print(p1name, ", Your score is: ", pp1)
    print(p2name, ", Your score is: ", pp2)
    print("Thanks for playing! ;)")


def create_question(movie):
    n= len(movie)
    letters= list(movie)
    temp=[]
    for i in range (n):
        if letters[i]==' ' :
            temp.append(' ')
        else:
            temp.append("-")
        qn=''.join(str(x) for x in temp)
    return qn
    
    
def is_present(let,movie):
    c=movie.count(let)
    if c==0 :
        return False
    else:
        return True
    
    
def unlock(qn,movie,let):
    ref=list(movie)
    qn_list= list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==let:
            temp.append(ref[i])
        else:
            if qn_list[i]=='-':
                temp.append('-')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new 
    
def play():
    p1name=input("Player 1, Enter your name: ")
    p2name=input("Player 2, Enter your name: ")
    pp1=0
    pp2=0
    turn=0
    
    while(1):
        if turn%2 == 0 :
            #player1
            print(p1name,", your turn!")
            picked_movie= random.choice(movies)
            qn= create_question(picked_movie)
            print(qn)
            modified_qn= qn
            
            not_said= True
            while(not_said):
                letter=input("Your Guess? ")
                if is_present(letter,picked_movie):
                    #unlock
                    modified_qn= unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    dec=int(input("Press 1 to guess the movie or 2 to guess another letter: "))
                    if dec==1 :
                        ans= input("Guess the movie: ")
                        if ans==picked_movie :
                            pp1+=1
                            print("Correct Answer!!", p1name, ", Your score is: ",pp1)
                            not_said=False
                        else:
                            print("Wrong Answer! Try guessing the letter again..")
                else:
                    print(letter, " not found!")
            choice=int(input("Enter 1 if you want to continue and 0 if you want to exit the game: "))
            if choice==0 :
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            #player2
            print(p2name,", your turn!")
            picked_movie=random.choice(movies)
            qn= create_question(picked_movie)
            print(qn)
            modified_qn= qn
            
            not_said= True
            while(not_said):
                letter=input("Your Guess? ")
                if is_present(letter,picked_movie) :
                    #unlock
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    dec=int(input("Press 1 to guess the movie or 2 to guess another letter: "))
                    if dec==1 :
                        ans= input("Guess the movie: ")
                        if ans==picked_movie :
                            pp2+=1
                            print("Correct Answer!!", p2name, ", Your score is: ",pp2)
                            not_said=False
                        else:
                            print("Wrong Answer! Try guessing the letter again..")
                else:
                    print(letter, " not found!")
            choice=int(input("Enter 1 if you want to continue and 0 if you want to exit the game: "))
            if choice==0 :
                thank(p1name,p2name,pp1,pp2)
                break
                    
            
            
        
        turn= turn+1
        
                
play()