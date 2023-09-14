"""
Question: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#Idea0: Brute force will run forever.

# Idea1: Optimal/Mathematical
# LCM on a collection of numbers is: commutative, associative and idempotent
# LCM(a, b) = a * b / gcd(a.b)
# LCM(a,b,c) = LCM(a,b) * c / gcd(LCM(a,b), ans)
import math
lcm = 1
for i in range(1, 21):
    lcm = (lcm * i) // math.gcd(lcm, i)
print(lcm)
