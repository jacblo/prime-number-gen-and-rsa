#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:10:21 2020

@author: y3
"""
import prime_calc_package
from prime_calc_package import prime3
x = int(input("what number to test? "))
primes = prime3(x-1)
print(primes)
prime = True
for z in primes:
    if x%z == 0:
        prime = False
        break
if prime:
    print(f"\n\n\n{x} is a prime number")

else:
    print(f"\n\n\n{x} is not a prime number")