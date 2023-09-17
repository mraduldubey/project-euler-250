# Problem 004
# Mathematical Approach

Our answer will be of the format xyzzyx since its product of two three digit numbers.
Since, its a palindrome, it should satisfy this format:
    ans = x * 10^5 + y * 10^4 + z * 10^3 + z * 10^2 + y * 10^1 + z * 10^0
    ans = 100001x + 10010y + 1100z
    ans = 11 (9091x + 910y + 100z)
    that means, the ans will be divisble by 11.
    i.e. ans = a * b, at least a or b should be divisible by 11

# Other optimization
1. For both i & j, go from 999 -> 100, if pdt < largestPal found yet, dont check smaller values.

# Further ?
- Check if pal check in numbers instead of string based check helps. 
