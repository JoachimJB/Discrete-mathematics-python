# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:47:00 2022

@author: Joachim
"""

from Diffie_Hellmann import public_keys

#def sigma_generator():



def encryption(msg, q, h, g):
    ct=[]
    


msg = "Hei du"
#Prime and Generator
P = 347
G = 50

#Alice
s = 189
key = public_keys(P, G, s)

print(key)