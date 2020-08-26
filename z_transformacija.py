# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:27:17 2020

@author: Ana
"""

import control
from math import sqrt

#Z transformacija prenosne funkcije :
#funkcija u S domenu

f=control.tf([1,1],[1,1,1])
print(f)

#funkcija u Z domenu

z=control.c2d(f,1)
print(z)

#Crtanje nula i polova:

control.pzmap(z, True, 'PZmap')

#Niz polova i nula:

a=control.pole(z)
print(a)
b=control.zero(z)
print(b)   

#Proveravamo da li je sistem stabilan ili nestabilan:
counter=0

for i in a :
    if(sqrt(i.real**2 + i.imag**2))<1: 
        counter += 1
 
#za svaki pol ispitujemo da li je moduo manji od 1, ako jeste povecavamo counter
#proci ce se kroz svaki pol, koliko god da ih ima, i povecati counter svaki put kad treba
#na kraju fja len nam pokazuje broj polova i ako je striktno jednaka counteru onda je sistem stabilan (konvergira)
#da je postojao samo jedan pol ciji moduo nije manji od jedan, counter bi bio bar za 1 manji od len(a)
#i onda sistem ne bi bio stabilan         
    
if len(a) == counter:
    print("Sistem je stabilan")
else:
    print("Sistem je nestabilan")