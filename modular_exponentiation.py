"""
File: modular_exponentiation.py
Author: Joachim Jamtvedt Børresen
Date: Decemember 4, 2022
Description: Efficiently calculates the remainder when an integer is raised to a power and divided by another integer using modular exponentiation.
"""



# -*- coding: utf-8 -*-

#Binary expansion Algorithm
#b: Base number (Generator), n: Exponent (Private key), m: (Modulo divisor) Prime
def modular_exponentiation(b: int, n: int, m: int):
    
    x=1
    #Converts to binary number
    n_bin=bin(n)
    #storing remainder
    power = b % m
    #Loops through the binary number and calculates each true bit from LSB to MSB
    for i in range(len(n_bin)-1,1,-1):
        #Updates x for each true bit
        if int(n_bin[i]) == 1:
            x = (x*power)%m
        #Updating the power variable for every bit, true and false
        power=(power*power)%m
    #Returning the final answer
    return x

#Driver code
"""
#Input variables
b = 3           #Base number
n = 10**84      #Exponent
m = 132         #Modulo divisor
print (modular_exponentiation(b, n, m))
"""
