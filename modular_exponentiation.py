# -*- coding: utf-8 -*-

#Input variables
b = 3           #Base number
n = 10**84      #Exponent
m = 132         #Modulo divisor


"""
Binary Expansion Algorithm
Function: (b^n)mod(m) calculator which converts the decimal type exponent
to binary and then performs the calculation on each true bit starting from LSB to MSB.
Updates the x variable for each true bit if reminder is present.
Skipping false bits, but updates the power variable for every bits, true or false.
"""

def modular_exponentiation(b: int, n: int, m: int):
    
    x=1
    n_bin=bin(n)
    power = b % m

    for i in range(len(n_bin)-1,1,-1):
        if int(n_bin[i]) == 1:
            x = (x*power)%m
            #print(x)
        power=(power*power)%m
    
    return x

#print (modular_exponentiation(b, n, m))