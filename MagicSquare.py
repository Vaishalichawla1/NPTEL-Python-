# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 02:47:12 2024

@author: Vaishali
"""

def magicSquare(n):
    magicSquare=[[0 for i in range(n)] for j in range(n)]
    #print(magicSquare)
    
    print("Initial Magic Square:")
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
        
    i=n//2
    j=n-1
    count=1
    
    while(count <= n*n):
        if(i == -1 and j == n):
            i=0
            j=n-2
        else:
            if(i<0):
                i=n-1
            if(j==n):
                j=0
        
        if(magicSquare[i][j]!=0):
            i+=1
            j=j-2
            continue
        else:
            magicSquare[i][j]=count
            count+=1
            
        i=i-1
        j=j+1
        
    print("Final Magic Square:")
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
    print("The Magic Number is "+str((n*(n**2+1))/2))
    
n=(int(input("Enter the order of Magic Square: ")))
magicSquare(n)   
