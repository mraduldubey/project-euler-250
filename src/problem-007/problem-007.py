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
import time

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
print("Optimized iterative sieve of eratothenes solution")
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
print("Optimized iterative sieve of eratothenes solution")
print(f"Real time: {t1[0] - t0[0]:.5f} secs")
print(f"CPU time: {t1[1] - t0[1]:.5f} secs")
print("------------")
