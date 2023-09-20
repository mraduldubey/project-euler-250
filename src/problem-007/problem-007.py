"""
Question: What is the 10001st prime number ?
"""
""" 
Solution Idea: Sieve. But the problem is we dont have a upper limit of number - we just have count of prime.
Idea2: Prime Number Theoram states that there are rough n/logn number of primes less than n but the distance b/w primes get randomly larger.
Since logn will be > 1, we can only hope to find it iteratively, lets start with 2,3,4,5... and so on till 10001st prime is found
So, we try a iterative model. We start with sieving till a rough estimate:
"""
import time
import math

N = 10001
primes = [False, False, True]
sievedUpto = 2 

def findNthPrime(regular=False):
    global N
    global primes
    factor = 2
    countOfPrimes = 0
    while countOfPrimes < N:
        n = factor * N
        if regular:
            sieve_regular(n)
        else:
            sieve(n)
        countOfPrimes = len([each for each in primes if each])
        factor += 1

    count = 0
    for i, each in enumerate(primes):
        if each:
            count += 1
        if count == N:
            return i

def findClosestMultipleToSievedUpto(p):
    global sievedUpto
    ratio = sievedUpto//p
    if ratio <= 1:
        return p+p
    return (sievedUpto//p)*p + p
    
def sieve(n):
    global primes
    global sievedUpto
    primes += [True] * (n - len(primes) + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            # we dont need to start from p*p because [p*p, prev n] has already been sieved
            closestMulFromSievedUpto = findClosestMultipleToSievedUpto(p)
            for i in range(closestMulFromSievedUpto, n+1, p):
                primes[i] = False
        p += 1
    sievedUpto = n

t0 = time.perf_counter(), time.process_time()
ans = findNthPrime()
t1 = time.perf_counter(), time.process_time()

print(ans)
print("Iterative \"supposedly optimized\" sieve of eratothenes solution")
print(f"Real time: {t1[0] - t0[0]:.5f} secs")
print(f"CPU time: {t1[1] - t0[1]:.5f} secs")
print("------------")


# Comparison against normal sieve.
def sieve_regular(n):
    global primes
    global sievedUpto
    primes += [True] * (n - len(primes) + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    sievedUpto = n

t0 = time.perf_counter(), time.process_time()
ans = findNthPrime(regular=True)
t1 = time.perf_counter(), time.process_time()

print(ans)
print("Iterative normal sieve of eratothenes solution")
print(f"Real time: {t1[0] - t0[0]:.5f} secs")
print(f"CPU time: {t1[1] - t0[1]:.5f} secs")
print("------------")

#Idea: Observations about primes
"""
1 is not a prime.
All primes except 2 are odd.
All primes greater than 3 can be written in the form 6k+/-1 i.e. (start with 5, keep adding 6, that number and number + 2 give us all possible nums in seq)
Any number n can have only one primefactor greater than sqrt(n) that implies the other factor must be <= sqrt(n) .
"""

def isPrime(n):
    if n == 1:
         return False
    elif n < 4:
        return True
    elif not n%2:
        return False
    elif n < 9:
        return True
    elif not n%3:
        return False
    else:
        # check only till sqrt(n)
        nRoot = math.sqrt(n)
        # start with 5 and check for every 6k+-1 number (even though some may not be prime themselves)
        # seq: 5 -> 11 (check for 11 & 13) -> 17 (check for 17 and 19) and so on...
        f = 5 # 6k +- 1
        while f <= nRoot:
            if not n%f:
                return False
            if not n%(f+2):
                return False
            f += 6
    return True

t0 = time.perf_counter(), time.process_time()
count = 1
candidate = 1
while True:
    candidate += 2 # no prime can be even
    if isPrime(candidate):
        count += 1
        if count >= N:
            break
t1 = time.perf_counter(), time.process_time()
print(ans)
print("Prime factorization based on 6k+-1 idea")
print(f"Real time: {t1[0] - t0[0]:.5f} secs")
print(f"CPU time: {t1[1] - t0[1]:.5f} secs")
print("------------")