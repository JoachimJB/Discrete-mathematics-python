"""
File: ElGamal_algorithm.py
Author: Joachim Jamtvedt Børresen
Date: Decemember 4, 2022
Description: ElGamal encryption and decryption
"""

# -*- coding: utf-8 -*-

from Diffie_Hellmann import *

#ElGamal encryption that generates and returns public key (C_g and encrypted text)
#p_key: Public key sent which includes P, G and public key
#x: Senders private key, y: message to be encrypted
def HE_encryption(p_key, x, y):
    ct=[]                                   #Encrypted msg array
    key_ct=[]                               #Return variable
    P, G, a = p_key[0], p_key[1], p_key[2]  #Assigns from argument p_key, which consists of 3 items
    C_a = secret_key(P, x, a)               #Generate shared secret key
    #print("C_a: ", C_a)                     
    C_g = public_key(P, G, x)
    #print("C_g: ", C_g)                     #Generates senders public key
    for i in range(0, len(y)):              #Converting each letter in msg (y) to index position in ct
        ct.append(y[i])
    for i in range(0,len(ct)):              #Encrypt each letter(index) of ct(y)
        ct[i]=C_a*ord(ct[i])
    key_ct = [C_g, ct]
    return key_ct                           #Returning array with new public key and subarray of uncrypted message


def HE_decryption(ct, P, G, x):
    pt=[]
    C_g = ct[0]
    C_a = secret_key(P, x, C_g)
    for item in ct[1]:
        pt.append(chr(int(item/C_a)))
    return pt


#Encryption algorithm
def encryption(M, P, a, G, y):
    ct=[]
    #x = public_key(P, G, a)
    kx = secret_key(P, a, y)                #Generate shared secret key
    for i in range(0, len(M)):              #Fillin up ct with message M
        ct.append(M[i])                     
    for i in range(0,len(ct)):              #Encrypt each letter of M
        ct[i]=kx*ord(ct[i])
    return kx, ct                           #Return shared secret key and encrypted message

#Decryption algorithm
def decryption(ct, P, a, G, y):
    pt=[]
    #x = public_key(P, G, a)
    kx = secret_key(P, a, y)                #Identical shared secret key generated with different private key
    for i in range(0, len(ct)):             #Decrypt each hash to a letter
        pt.append(chr(int(ct[i]/kx)))
    return pt

