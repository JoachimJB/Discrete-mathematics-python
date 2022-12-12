# -*- coding: utf-8 -*-

from modular_exponentiation import modular_exponentiation

#Compute public keys
#P: Prime, G: Generator, a: Private key
def public_key(P, G, a):
    x = modular_exponentiation(G, a, P)
    return x

#Compute symmetric key (secret key)
#P: Prime, a: Private key, y: Other persons public key
def secret_key(P, a, y):
    #ka = y**a % P
    ka = modular_exponentiation(y, a, P)
    return ka

#For generating public keys for two persons in the same function
def public_keys(P, G, a, b):
    x = modular_exponentiation(G, a, P)
    y = modular_exponentiation(G, b, P)
    return x,y   

#For generating shared secret keys for two persons in the same function
#Compute symmetric keys (secret keys)
def secret_keys(P, a, b, x, y):
    ka = y**a % P
    kb = x**b % P
    return ka, kb

#Driver code
"""
P = 23
G = 9

x_a = 4
x_b = 3

public_key_alice = public_key(P, G, x_a)
public_key_bob = public_key(P, G, x_b)
print(public_key_alice)
print(public_key_bob)
"""



