# -*- coding: utf-8 -*-

from Diffie_Hellmann import *

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

