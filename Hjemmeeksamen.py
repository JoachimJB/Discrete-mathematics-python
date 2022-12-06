# -*- coding: utf-8 -*-

import random
from ElGamal_algorithm import *

#Driver code
M = "Hjemmeksamen 2022"             #Message to be encrypted and sent to Bob

P = 2**61 - 1                       #Large Prime 
G = 8495135451210                   #Generator in the finite cyclic group of order P

a_x = random.randint(1, P-1)        #Private key only known to Alice (In range of [1, P-1])
b_x = random.randint(1, P-1)        #Private key only known to Bob (In range of [1, P-1])

a_key = public_key(P, G, a_x)       #Alice generates public key: a:= g^a_x. From Diffie_Hellmann.py
b_key = public_key(P, G, b_x)       #Bob generates public key: b:= g^b_x. From Diffie_Hellmann.py

public_key_Alice = [P, G, a_key]    #Public key Alice (ElGamal protocol)   
public_key_Bob = [P, G, b_key]      #Public key Bob (ElGamal protocol)   

print("Public key Alice (P, G, a):", public_key_Alice)  
print("Public key Bob (P, G, b):", public_key_Bob)  

#Encryption
#Bob is encrypting a message which is to be sent to Bob. Using all public keys + his private key
#M: Message, P: Large Prime, b_x: Bob privat key, G: Generator, a_key: Alice public key
kx, ct = encryption(M, P, b_x, G, a_key)    #From ElGamal_Algorithm.py
print("Encrypted message (M): ", ct)

#Bob is decrypting the message received from Alice using all public keys + his private key
#M: Message, P: Large Prime, a_x: Alice privat key, G: Generator, b_key: Bob public key
pt = decryption(ct, P, a_x, G, b_key)   #From ElGamal_Algorithm.py
d_M = ''.join(pt)                       #Convert list to string for pretty output
print("Decrypted message (M): ", d_M)