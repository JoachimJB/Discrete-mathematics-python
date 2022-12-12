# -*- coding: utf-8 -*-

import random
from ElGamal_algorithm import *
from Prime_numbers import *

#Driver code
M = "Hjemmeksamen 2022"             #Message to be encrypted and sent to Bob

P = 2**61 - 1                       #Large Prime 
G = 8495135451210                   #Generator in the finite cyclic group of order P

a_x = random.randint(1, P-1)        #Private key only known to Alice (In range of [1, P-1])
"""
#Metode for å finne størst mulig prime innenfor a_x oppgitt. For treg over 9 siffer
for i in range(a_x, 0, -1):         #Starter på a_x og prøver a_x - 1, osv om a_x ikke er prime
    if prime_check(i):
        a_x = i
        break
"""
b_x = random.randint(1, P-1)        #Private key only known to Bob (In range of [1, P-1])
"""
#Metode for å finne størst mulig prime innenfor a_x oppgitt. For treg over 9 siffer
for i in range(b_x, 0, -1):
    if prime_check(i):
        b_x = i
        break
"""

a_key = public_key(P, G, a_x)       #Alice generates public key: a:= g^a_x. From Diffie_Hellmann.py
b_key = public_key(P, G, b_x)       #Bob generates public key: b:= g^b_x. From Diffie_Hellmann.py

public_key_Alice = [P, G, a_key]    #Public key Alice (ElGamal protocol)   
public_key_Bob = [P, G, b_key]      #Public key Bob (ElGamal protocol)   

print("Public key Alice (P, G, a):", public_key_Alice)  
print("Public key Bob (P, G, b):", public_key_Bob)  

#Encryption
#Bob is encrypting a message which is to be sent to Alice. Using all public keys + his private key
#public_key_Alice: Includes P, G and her public key, b_x: Bob privat key, M: Message
Cg_Cy = HE_encryption(public_key_Alice, b_x, M)     #Calling function in ElGamal_Algorithm.py
print("Encrypted message (Cy, with public key): ", Cg_Cy)

#Decryption
#Alice is decrypting the message received from Bob using all public keys + her private key
#Cg_Cy: Bob's public key + encrypted msg, P: Large Prime, G: Generator, a_x: Alice privat key
Cy_decrypt = HE_decryption(Cg_Cy, P, G, a_x)        #Calling function in ElGamal_Algorithm.py
d_y = ''.join(Cy_decrypt)                           #Convert list to string for pretty output
print("Decrypted message (M): ", d_y)


#Below is V1.0 when not sending (Cg, Cy) togheter to receiver:
"""
#Encryption
#Bob is encrypting a message which is to be sent to Alice. Using all public keys + his private key
#M: Message, P: Large Prime, b_x: Bob privat key, G: Generator, a_key: Alice public key
kx, ct = encryption(M, P, b_x, G, a_key)    #From ElGamal_Algorithm.py
print("Encrypted message (M): ", ct)

#Decryption
#Alice is decrypting the message received from Bob using all public keys + her private key
#M: Message, P: Large Prime, a_x: Alice privat key, G: Generator, b_key: Bob public key
pt = decryption(ct, P, a_x, G, b_key)   #From ElGamal_Algorithm.py
d_M = ''.join(pt)                       #Convert list to string for pretty output
print("Decrypted message (M): ", d_M)
"""