# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:35:11 2020

@author: jacob b
"""
import random
from numba import jit, cuda 
import numpy as np 
#miller_rabin is a primality test
def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

#gcd = greatest common diviser
def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
"""
a function that uses miller rabin's primality test to genarate a prime number in a certain number of bits length
in other words you give it a number of bits and you will get a prime number with that number of bits
"""

def genprime(k):
    x = ""
    k = int(k)
    for y in range(k):
        x = x + "1"
    y = "1"
    for z in range(k-1):
        y = y + "0"
    x = int(x,2)
    y = int(y,2)
    p = 0
    while True:
        p = random.randrange(y,x)
        if miller_rabin(p,40):
            break
    return p

#Extended great common divisor
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#Modular multiplicative inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


#key genaration k = number of bits must be power of 2
@jit
def gennarate_keys(k):
    if k % 2 == 1:
        raise ValueError("k must be even")
    #gen p
    p = genprime(k/2)
    #gen q
    q = 0
    while True:
        q = genprime(k - k/2)
        if q != p:
            break
    
    n = p*q
    l = (p-1)*(q-1)
    
    #gen e
    for e in range(2,l): 
        if gcd(e,l)== 1: 
            break
    
    d = modinv(e,l)
    return((n,e),int(d))
  
#encrypt an integer - easier to make this and call it then to code it every time because i might make a mistake
def ecryptnum(message,n,e):
    return pow(message,e,n)

#same as encryption integer but decryption
def decryptnum(crypt,n,d):
    return pow(crypt,d,n)

#i devided encryption to 2 functions pretty arbitrarily because i wrote this first
def encryptTextToList(text,n,e):
    out = []
    for x in text:
        out.append(ecryptnum(ord(x),n,e))
    return out
#add's commas between and makes string
def encryptText(text,n,e):
    x = encryptTextToList(text,n,e)
    out = []
    for z in x:
        out.append(str(z))
    return ",".join(out)

#divides by commas and the decrypts it and then makes a string
def decryptText(crypt,n,d):
    x = crypt.split(",")
    y = []
    out = ""
    for z in x:
        y.append(int(z))
    for x in y:
        out = out + chr(decryptnum(x,n,d))
    return out

