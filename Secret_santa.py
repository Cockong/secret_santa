# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:34:48 2018

@author: rthie
"""
import random

def draw_names(donneurs):

    cadeau={}
    n=len(donneurs)
    recepteurs=donneurs+[]
    for prenom in donneurs[:n-1] :
        while True :
            i=random.randint(0,len(recepteurs)-1)        
            if  recepteurs[i]!=prenom:
                break    
        cadeau[prenom]=recepteurs[i]
        recepteurs.remove(recepteurs[i])
        
    if recepteurs[0]==donneurs[n-1]:
        print("error")
        i=random.randint(0,n-2)
        cadeau[recepteurs[0]]=donneurs[i]        
        for prenom in cadeau:
            if cadeau[prenom]==donneurs[i]:
                cadeau[prenom]=recepteurs[0]
                break
    else:
        cadeau[donneurs[n-1]]=recepteurs[0]
        
    for prenom in cadeau:
        assert(cadeau[prenom]!=prenom)
    assert(len(cadeau)==n)    
    return cadeau
 
def send_names(cadeau):
    for prenom in cadeau :
        a=open(prenom + ".txt","w")
        a.write(cadeau[prenom])
        a.close()

def test():
    donneurs=["remi","pierre","paul","jean","jacques","alphonse","jean_claude"]
    cadeau=draw_names(donneurs)
    send_names(cadeau)
test()




#open("santa)