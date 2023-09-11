n = 1000

# Brute force
s = 0
for i in range(1, n):
    if not i%5:
        s += i
        continue
    if not i%3:
        s += i
print(s)

# Optimal 1: dont iterate over all elements aka hop
s = 0
for i in range(3, n+1, 3): 
    s += i
for i in range(5, n+1, 5): 
    s += i
for i in range(15, n+1, 15): 
    s -= i
print(s)

# Optimal 2: Mathematical aka why we are here
# Idea1: number of elems div by x below y, nDivisible = y / x. 
# Idea2: 3 + 6 + 9 + 12 == 3 * (1 + 2 + 3 + 4) = 3 * (sum of natural numbers till nDivisible)
# Relates to the idea of triangular numbers (https://en.wikipedia.org/wiki/Triangular_number?oldformat=true)
a = n // 3
b = n // 5
c = n // 15
sa = (a * (a+1)) // 2
sb = (b * (b+1)) // 2
sc = (c * (c+1)) // 2
s = 3*sa + 5*sb - 15*sc
print(s)