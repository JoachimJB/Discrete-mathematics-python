# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:09:37 2022

@author: Joachim
"""
from ElGamal_algorithm import *

#Driver code
msg = "Hei  dobbel"

#Prime and Generator
P = 23
G = 9

#Alice
a_s = 4
a_key = public_key(P, G, a_s) #(power)

#Bob
b_s = 3
b_key = public_key(P, G, b_s) #(power)

print("Prime and Generator: ", P, G)
print("Alice public key: ", a_key)
print("Bob public key: ", b_key)

#Encryption
#Encrypt message using alice's keys
ct = encryption(msg, P, a_s, G, b_key)
print("Encrypted msg: ", ct)

#Decrypt message using bob's keys
pt = decryption(ct, P, b_s, G, a_key)
d_msg = ''.join(pt)
print("Decrypted msg: ", d_msg)