"""
Question:
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
#Idea: Mathematical
# square of (sum of first N natural nos) - sum of squares of first N natual nos
N = 100
ans = (pow(N,2) * pow(N+1,2))//4 - (N* (N+1) * (2*N + 1))//6
print(ans)