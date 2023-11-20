"""
File: Euclidean_Algorithm.py
Author: Joachim Jamtvedt Børresen
Date: Decemember 4, 2022
Description: Finding the greatest common divisor (GCD) of two integers.
"""

# -*- coding: utf-8 -*-

from colorama import Fore, Style

#Using the euclidean algorithm to find the greatest common divider
#Using while loop
def gcd(a, b):
    l = max(a,b)
    s = min(a,b)
    rest = l % s
    kvotient = l // s
    print(Fore.RED + "Greatest common divisor", Fore.CYAN + "Remainder", Style.RESET_ALL)
    print("Start:\t\tgcd(",l,",",s,")\t\t\tgir:", l, "=", Fore.RED + str(s), Style.RESET_ALL + "*", 
          kvotient, "+", Fore.CYAN + str(rest), Style.RESET_ALL)
    i=0
    while rest:
        l = s
        s = rest
        rest = l%s
        kvotient = l//s
        i+=1
        print("Iter",i,":\tgcd(",Fore.RED + str(l), Style.RESET_ALL,",",Fore.CYAN + str(s), Style.RESET_ALL + ")\t\t\tgir:", 
              l, "=", Fore.RED + str(s), Style.RESET_ALL + "*", 
                    kvotient, "+", Fore.CYAN + str(rest), Style.RESET_ALL)
    print("Answer:\t\tgcd(",a,",",b,") =", Fore.RED + str(s), Style.RESET_ALL)
   
#Using recursive function
def gcd_2(a, b):
    l = max(a,b)
    s = min(a,b)
    if s == 0:
        return a, b
    
    rest = l%s
    kvotient = l//s
    print("gcd(",Fore.RED + str(l), Style.RESET_ALL,",",Fore.CYAN + str(s), Style.RESET_ALL + ")\t\tgir:", 
          l, "=", Fore.RED + str(s), Style.RESET_ALL + "*", 
                kvotient, "+", Fore.CYAN + str(rest), Style.RESET_ALL)
    l = s
    
    gcd_2(l, rest)


#Extended euclidean algorithm recursively
def gcd_ext(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x_t, y_t = gcd_ext(b%a, a)
    
    x = y_t - (b//a) * x_t
    y = x_t
    
    return gcd, x, y
    

#Driver code

a, b = 29,179

#Extended Euclidean Algorithm
g, x, y = gcd_ext(a, b)
print("Extended Euclidean Algorithm")
print("gcd(",a ,",", b,") = ",g)

#Euclidean Algorithm
print("Euclidean Algorithm")
gcd_2(a, b)
