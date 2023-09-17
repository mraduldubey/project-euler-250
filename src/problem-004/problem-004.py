"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

# Idea1: Optimally check pal using string n/2 comparisons, check all numbers
pals = set()
def checkPalStr(val):
    if val in pals:
        return True
    valStr = str(val)
    if len(valStr) & 1:
        l = len(valStr) // 2
        r = l
    else:
        l = (len(valStr) // 2) - 1
        r = l + 1
    
    while l >= 0 and r < len(valStr):
        if valStr[l] != valStr[r]:
            return False
        l -= 1
        r += 1
    pals.add(val)
    return True

t1 = time.perf_counter(), time.process_time()
# Note: the order of checking does not matter. It can be [100-999] as well.
# There is no guarentee of finding the largest number this way.
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        pdt = i * j
        checkPalStr(pdt)
print(max(pals))
t2 = time.perf_counter(), time.process_time()

print(f"Solution1")
print(f"Real Time: {t2[0]-t1[0]:.5f} seconds")
print(f"CPU Time: {t2[1]-t2[1]:.5f} seconds")
print("---------------")

# Idea2: Optimal: Find largest number and stop
largestPal = 0
t1 = time.perf_counter(), time.process_time()
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        pdt = i * j
        if pdt < largestPal: #no point in checking smaller b values
            break
        if checkPalStr(pdt):
            largestPal = pdt
print(largestPal)
t2 = time.perf_counter(), time.process_time()

print(f"Solution2: Optimized ")
print(f"Real Time: {t2[0]-t1[0]:.5f} seconds")
print(f"CPU Time: {t2[1]-t2[1]:.5f} seconds")
print("---------------")

#Idea3: Mathematical - Filter out some numbers based on mathematical observation
"""
Our answer will be of the format xyzzyx since its product of two three digit numbers.
Since, its a palindrome, it should satisfy this format:
    ans = x * 10^5 + y * 10^4 + z * 10^3 + z * 10^2 + y * 10^1 + z * 10^0
    ans = 100001x + 10010y + 1100z
    ans = 11 (9091x + 910y + 100z)
    that means, the ans will be divisble by 11.
    i.e. ans = a * b, at least a or b should be divisible by 11
"""
largestPal = 0
t1 = time.perf_counter(), time.process_time()
for i in range(999, 99, -1):
    if i % 11 == 0:
        # i is multiple of 11 i.e. j might not be not
        j = 999
        delta = 1
    else:
        # i is not multiple of 11 i.e. j must be
        j = 990 # smallest num < 999 that is div by 11
        delta = 11
    while j >= i:
        pdt = i * j
        if pdt < largestPal: #no point in checking smaller b values
            break
        if checkPalStr(pdt):
            largestPal = pdt
        j -= delta
print(largestPal)
t2 = time.perf_counter(), time.process_time()

print(f"Solution3: Factor of 11")
print(f"Real Time: {t2[0]-t1[0]:.5f} seconds")
print(f"CPU Time: {t2[1]-t2[1]:.5f} seconds")
print("---------------")
