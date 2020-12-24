# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:20:58 2020

@author: Seyhan-Beryhan
"""
user = list()
user.append(input("first name:" ))
user.append(input("last name:" ))
user.append(int(input("age:" )))
user.append(int(input("birth year:" )))


if user[2] < 18:
        print("you can't go out because it's too dangerous")
elif user[2] >= 18:
        print("you can go out the street") 

        
for i in user:
    print(i)
    
   