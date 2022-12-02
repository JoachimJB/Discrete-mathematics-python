# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:24:51 2022

@author: Joachim
"""

def prime_check(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            return n

def mersenne_prime(p):
    if prime_check(p):
        M = 2**p-1
        M_2 = 2*p - 1
        if prime_check(M):
            print("Mersenne prime:", M)
        else:
            print("Composite mersenne number", M)
    else:
        print("No prime entered")
    
    
#mersenne_prime(11)