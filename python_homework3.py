# -*- coding: utf-8 -*-

"""
Created on Fri Dec 25 14:48:27 2020


"""

name = "gamer"
print ("hello  {}  "  .format(name))
import random 

word = ["python", "machine", "computer", "web", "programming"]
word = random.choice(word)

guess = 5 
letters = []
x = len(word)
z = list ('_' * x)
print('_' .join(z), end='\n')

while guess > 0:
    y= input("please guess a letter:" )
    if y in letters:
     print ("Please do not guess the letters you guessed earlier")
     continue
    elif len (y) > 1:
        print ("please entered a just letter")
        continue
    elif y not in word :
        guess -= 1 
        print ("wrong guess {} you have the right to guess" .format(guess))
    else:
        for i in range (len(word)):
            if y== word[i] :
                print("correct guess!")
                z[i]= y 
                letters.append (y)
                print (' ' .join(z), end='\n')
                break


    if guess==0:
     print("you are out of gueswork. you lost! the man hanged")
    
                  


         
             
     
 
 
               
                
        

