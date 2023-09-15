# Idea1: Sieve of Eratothenes
- use sieve of eratothenes to generate primes till N
- go backwards and check for divisibility
- FAILED - Memory error for such a huge number. Eratothenes needs an array for N size. Even using bit array will be same order. 

# Idea2: Repeated division by smallest prime factor
- N, find smallest prime factor of N by going from [2, sqrt(N)]. Lets call it p
- Divide, N by p, giving the new number to be divided
- Repeat,
- Collection of the p numbers are all the prime factors **in the ascending order**
- Or, the last number where p == N, is the largest prime factor.

# Conclusion
- Sieve is more useful for cases where we need to generate a list of prime numbers in a range. 
- Its not a good idea to implement sieve for finding prime factors of a number. Complexity: (O(n log(log(n))))
- Better approach is repeated division by smallest prime factors of the resulting number, complexity: O(sqrt(n))
