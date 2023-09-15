"""
What is the largest prime factor of the number 600851475143?
"""

"""
#Idea: Use sieve to generate primes till N, check in reverse order for divisibility
import math 
N = 600851475143  # (>6 BILLION)
rootN = math.ceil(math.sqrt(N))
# using boolean array
isPrime = [True, True] + [False] * (N-2) #Untenable: Memory Error (~600GB required)
for i in range(2, rootN+1):
    if isPrime[i]:
        j = i * i
        while j < N:
            isPrime[j] = 0
            j = j + i
print(len(isPrime))
# go from bwd
for i in range(N-1, -1, -1):
    print(i)
    if isPrime[i] and (N % i) == 0:
        print(i)
        break
"""

# Idea2: Keep diving the number by the smallest prime factor. The last number will be largest prime factor of N.
# Complexity: O(sqrt(N))
import math

N = 600851475143

def smallest_prime_factor(num):
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return i
    return num # its prime

while True:
    p = smallest_prime_factor(N)
    print(p) # print all prime factors of N
    if p < N:
        N = N // p
    elif p == N:
        print("ans:", p)
        break