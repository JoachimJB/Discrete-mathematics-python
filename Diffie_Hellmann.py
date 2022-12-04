# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:00:58 2022

@author: Joachim
"""

from modular_exponentiation import modular_exponentiation

#Compute public keys
#P: Prime, G: Generator, a: Private key
def public_key(P, G, a):
    x = modular_exponentiation(G, a, P)
    return x

#Compute symmetric key (secret key)
#P: Prime, a: Private key, y: Other persons public key
def secret_key(P, a, y):
    ka = y**a % P
    return ka

def public_keys(P, G, a, b):
    x = modular_exponentiation(G, a, P)
    y = modular_exponentiation(G, b, P)
    return x,y   

#Compute symmetric keys (secret key)
def secret_keys(P, a, b, x, y):
    ka = y**a % P
    kb = x**b % P
    return ka, kb