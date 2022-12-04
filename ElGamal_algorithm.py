# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:47:00 2022

@author: Joachim
"""

from Diffie_Hellmann import *

def encryption(msg, P, a, G, y):
    ct=[]
    x = public_key(P, G, a)
    kx = secret_key(P, a, y)
    for i in range(0, len(msg)):
        ct.append(msg[i])
    for i in range(0,len(ct)):
        ct[i]=kx*ord(ct[i])
    return ct

def decryption(ct, P, a, G, y):
    pt=[]
    x = public_key(P, G, a)
    kx = secret_key(P, a, y)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i]/kx)))
    return pt

