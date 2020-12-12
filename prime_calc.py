# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:55:55 2020

@author: jb
"""
import time
from random import randint
import random

                          
def prime1(rangeprime):
    nums = []
    primes = []
    for x in range(rangeprime):
        nums.append(x)
    is_prime = False
    for y in nums:
        if y == 0:
            is_prime = False
        elif y == 1:
            is_prime = False
        else:
            is_prime = True
            for x in nums[2:y-1]:
                if y % x == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(y)
           
    return primes

                          
def prime2(rangeprime):
    nums = []
    primes = []
    for x in range(rangeprime):
        nums.append(x)
    is_prime = False
    for y in nums:
        if y == 0:
            is_prime = False
        elif y == 1:
            is_prime = False
        elif y == 2:
            is_prime = True
            primes.append(y)
        elif y == 3:
            is_prime = True
            primes.append(y)
        elif y == 4:
            is_prime = False
        elif y == 5:
            is_prime = True
            primes.append(y)
        
        else:
            is_prime = True
            for x in nums[2 : int(round(y/2, 0))]:
                if y % x == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(y)
           
    return primes    

                          
def prime3(rangeprime):
    nums = []
    primes = []
    for x in range(rangeprime):
        nums.append(x)
    is_prime = False
    for y in nums:
        if y == 0:
            is_prime = False
        elif y == 1:
            is_prime = False
        else:
            is_prime = True
            for x in primes:
                if y % x == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(y)
    
    return primes

 
def prime4(rangeprime):
    nums = []
    primes = []
    for x in range(rangeprime):
        nums.append(x)
    is_prime = False
    for y in nums:
        if y == 0:
            is_prime = False
        elif y == 1:
            is_prime = False
        else:
            is_prime = True
            for x in primes[:int(round(len(primes)/2,0))]:
                if y % x == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(y)
    
    return primes


 
def actual_sive(rangeprime):
    x = []
    out = []
    counter = 0
    for z in range(2,rangeprime+1):
        x.append(z)
    for z in x:
        if z == None:
            counter += 1
            continue
        for w in x[:z-1]:
            if w == None:
                continue
            if z % w == 0 and z != w and z > w:
                x[counter] = None
        counter += 1
    for w in x:
        if w != None:
            out.append(w)
    return out

 
def prime8(rangeprime):
    primes = []
    is_prime = False
    for y in range(rangeprime):
        if y == 0:
            is_prime = False
        elif y == 1:
            is_prime = False
        else:
            is_prime = True
            for x in primes:
                if y % x == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(y)
    
    return primes
    
 
def isProbablyPrime(n, k = 5):
    if (n < 2 ):
        return False
    output = True
    for i in range(0, k):
        a = randint(1, n-1)
        if (pow(a, n-1, n) != 1):
            return False 
    return output

 
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

time1 = 0
time2 = 0
time3 = 0
time4 = 0
time5 = 0
time6 = 0


x = int(input("up to what number to calc? "))
startorskip = input("start first or skip? start / skip ")
if startorskip.lower() == "start":
    print("calculating...(test all numbers that are smaller)")
    timea = time.time()
    print(prime1(x))
    timeb = time.time()
    time1 = timeb - timea
elif startorskip.lower() == "skip":
    time1 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()

startorskip = input("start next or skip? start / skip ")
if startorskip.lower() == "start":
    print("calculating...(test half numbers)")
    timea = time.time()
    print(prime2(x))
    timeb = time.time()
    time2 = timeb - timea
elif startorskip.lower() == "skip":
    time2 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()

startorskip = input("start next or skip? start / skip ")
if startorskip.lower() == "start":
    print("calculating...(Sieve of Eratosthenes)")
    timea = time.time()
    print(prime3(x))
    timeb = time.time()
    time3 = timeb - timea
elif startorskip.lower() == "skip":
    time3 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()

startorskip = input("start next or skip? start / skip ")
if startorskip.lower() == "start":
    print("calculating...(Sieve of Eratosthenes up to half)")
    timea = time.time()
    print(prime4(x))
    timeb = time.time()
    time4 = timeb - timea
elif startorskip.lower() == "skip":
    time4 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()   

startorskip = input("start next or skip? start / skip ")
if startorskip.lower() == "start":
    print("calculating...(actual Sieve of Eratosthenes)")
    timea = time.time()
    print(actual_sive(x))
    timeb = time.time()
    time10 = timeb - timea
elif startorskip.lower() == "skip":
    time10 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()

startorskip = input("start next or skip? start / skip ")
if startorskip.lower() == "start":
    print("calculating...(better Sieve of Eratosthenes)")
    timea = time.time()
    print(prime8(x))
    timeb = time.time()
    time8 = timeb - timea
elif startorskip.lower() == "skip":
    time8 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()

startorskip = input("start next or skip? start / skip ")
if startorskip.lower() == "start":
    p = int(input("what number should i test with fermants little therum? "))
    print("calculating...")
    timea = time.time()
    if isProbablyPrime(p):
        timeb = time.time()
        print(f"the number {p} is probobly a prime")
        z = input("should i check? y/n ")
        if z == "y":
            print('testing... might take a while')
            is_prime = True
            nums = []
            for x in range(p-1):
                nums.append(x)
            for x in nums[2:]:
                if p == 0:
                    is_prime = False
                elif p == 1:
                    is_prime = False
                elif p % x == 0:
                    print("it is not a prime")
                    is_prime = False
                    break
            if is_prime:
                print(f"the number {p} is indeed a prime")
                    
            
        elif z == "n":
            print("ok")
    
    else:
        timeb = time.time()
        print(f"the number {p} is not a prime.")
    
    time5 = timeb - timea
    
elif startorskip.lower() == "skip":
    time4 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()   

startorskip = input("start next or skip? start / skip ")
if startorskip.lower() == "start":
    p = int(input("what number should i test with miller rabin's primality test? "))
    y = int(input("how many iterations to test? "))
    print("calculating...")
    timea=0
    timeb=0
    timec=0
    timed=0
    timea = time.time()
    if miller_rabin(p,y):
        timeb = time.time()
        print(f"the number {p} is probobly a prime")
        z = input("should i check? y/n ")
        if z == "y":
            timec = time.time()
            print('testing... might take a while')
            is_prime = True
            nums = []
            for x in range(p-1):
                nums.append(x)
            for x in nums[2:]:
                if p == 0:
                    is_prime = False
                elif p == 1:
                    is_prime = False
                elif p % x == 0:
                    print("it is not a prime")
                    is_prime = False
                    break
            if is_prime:
                print(f"the number {p} is indeed a prime")
            timed = time.time()        
            
        elif z == "n":
            print("ok")
    
    else:
        timeb = time.time()
        print(f"the number {p} is not a prime.")
    
    time6 = (timeb - timea) + (timed - timec)
    
elif startorskip.lower() == "skip":
    time4 = "skipped"
else:
    print("you didnt input valid input - quiting...")
    quit()   

input("next")

print(f"\nthe first (test all numbers that are smaller) had a time of {time1} seconds\nthe second (test half numbers) had a time of {time2} seconds\nthe third (Sieve of Eratosthenes edited) had a time of {time3} seconds\nthe forth (Sieve of Eratosthenes edited up to half) had a time of {time3} seconds\nactual sive of Eratosthenes had a time of {time10}\nbetter then my og sive had a time of {time8}\nfermat's little theorem had a time of {time5} seconds\nmiller rabin's primality test had a time of {time6} seconds")

input("press any key to quit")