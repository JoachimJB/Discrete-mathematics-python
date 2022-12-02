# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:00:58 2022

@author: Joachim
"""

from modular_exponentiation import modular_exponentiation

#Compute public keys
#P, G public keys, a, b private keys

def public_keys(P, G, s):
    x = modular_exponentiation(G, s, P)
    return x

"""
def public_keys(P, G, a, b):
    x = modular_exponentiation(G, a, P)
    y = modular_exponentiation(G, b, P)
    return x,y   

#Compute symmetric keys (secret key)
def secret_keys(P, a, b, x, y):
    ka = y**a % P
    kb = x**b % P
    return ka, kb
"""
#public keys
#P = 23
#G = 9

#private keys
#alice_p = 4
#bob_p = 3