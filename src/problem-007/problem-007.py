"""
Question: What is the 10001st prime number ?
"""
""" 
Solution Idea: Sieve. But the problem is we dont have a upper limit of number - we just have count of prime.
Idea2: Prime Number Theoram states that there are rough n/logn number of primes less than n but the distance b/w primes get randomly larger.
So, we try a iterative model. We start with sieving till a rough estimate:
n = 10001 * logn
Lets say, n = 1001 * 2 and keep doubling every time we run short. 
"""


import math
 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = 10000
primes = [False, False, True]
sievedUpto = 2 

def findNthPrime():
    global N
    factor = 2
    countOfPrimes = 0
    while countOfPrimes < N + 1:
        n = factor * N
        sieve(n)
        countOfPrimes = len([each for each in primes if each])
        factor += 1
    
    count = 1
    for i, each in enumerate(primes):
        if each:
            if not is_prime(i):
                print("GOT YAAAA", i, count)
                #raise Exception()
            count += 1
        if count == N+1:
            print("count", count)
            print("diff", 104743 - i)
            return i
            break

def findClosestMultipleToSievedUpto(p):
    global sievedUpto
    if p == 2: # the only even prime
        if sievedUpto == 2:
            return 4
        else:
            return ((sievedUpto // p) + 1)*p
    else:
        return ((sievedUpto // p) + 1)*p + p
    
def sieve(n):
    global primes
    global sievedUpto

    primes += [True] * (n - len(primes) + 1)
    print("len" ,len(primes))
    p = 2
    while p * p <= n:
        #print("is it prime ?", p, primes[p], p*p, n)
        if primes[p]:
            #print(p)
            # we dont need to start from p*p because [p*p, prev n] has already been sieved. 
            # So, start from the closest multiple of p to the number that we previously sieved upto
            closestMulFromSievedUpto = findClosestMultipleToSievedUpto(p)
            print("closest to ", sievedUpto, p, "->", closestMulFromSievedUpto)
            for i in range(closestMulFromSievedUpto, n+1, p):
                primes[i] = False
                if (i == 2264):
                    print("AHHHHHHHHHHHHHHHH", p, i)
                    #raise Exception()
            print("P==>", p)
        p += 1
    sievedUpto = n
    print("sievedUpto", sievedUpto)

ans = findNthPrime()
print(ans)